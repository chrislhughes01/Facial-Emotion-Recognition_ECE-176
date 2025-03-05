import { useRef, useEffect, useState } from "react";

export default function WebcamFeed() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [isCameraOn, setIsCameraOn] = useState(false);
  const [emotion, setEmotion] = useState("Detecting...");
  const [probabilities, setProbabilities] = useState({});

  useEffect(() => {
    if (isCameraOn) {
      navigator.mediaDevices
        .getUserMedia({ video: true })
        .then((stream) => {
          if (videoRef.current) {
            videoRef.current.srcObject = stream;
          }
        })
        .catch((error) => console.error("Error accessing webcam:", error));
    } else {
      if (videoRef.current && videoRef.current.srcObject) {
        let stream = videoRef.current.srcObject;
        let tracks = stream.getTracks();
        tracks.forEach((track) => track.stop());
        videoRef.current.srcObject = null;
      }
    }
  }, [isCameraOn]);

  const captureFrame = async () => {
    if (!isCameraOn || !videoRef.current || !canvasRef.current) return;

    const canvas = canvasRef.current;
    const context = canvas.getContext("2d");
    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;
    context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(async (blob) => {
      const formData = new FormData();
      formData.append("file", blob, "frame.jpg");

      try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
          method: "POST",
          body: formData,
        });

        const data = await response.json();
        if (data.error) {
          console.error("Prediction error:", data.error);
        } else {
          setEmotion(data.emotion);
          setProbabilities(data.probabilities);
        }
      } catch (error) {
        console.error("Error sending frame:", error);
      }
    }, "image/jpeg");
  };

  useEffect(() => {
    const interval = setInterval(() => {
      captureFrame();
    }, 1000);
    return () => clearInterval(interval);
  }, [isCameraOn]);

  return (
    <div className="flex flex-col items-center space-y-4 p-4 bg-gray-900 text-white min-h-screen">
      <div className="relative">
        <video ref={videoRef} autoPlay className="w-96 h-auto rounded-lg shadow-md" />
        <canvas ref={canvasRef} style={{ display: "none" }} />
        <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 bg-black bg-opacity-70 text-white px-4 py-2 rounded-lg">
          <h2 className="text-xl font-bold">{emotion}</h2>
        </div>
      </div>

      <div className="w-96 bg-gray-800 p-4 rounded-lg shadow-lg">
        <h3 className="text-lg font-semibold text-center mb-2">Confidence Levels</h3>
        {Object.entries(probabilities).map(([label, prob]) => (
          <div key={label} className="mb-2">
            <div className="flex justify-between">
              <span>{label}</span>
              <span>{(prob * 100).toFixed(2)}%</span>
            </div>
            <div className="w-full bg-gray-700 rounded-lg overflow-hidden">
              <div
                className="bg-blue-500 h-2"
                style={{ width: `${prob * 100}%` }}
              />
            </div>
          </div>
        ))}
      </div>

      <button
        onClick={() => setIsCameraOn(!isCameraOn)}
        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
      >
        {isCameraOn ? "Turn Off Camera" : "Turn On Camera"}
      </button>
    </div>
  );
}
