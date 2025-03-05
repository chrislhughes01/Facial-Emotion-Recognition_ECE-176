import { useRef, useEffect, useState } from "react";

export default function WebcamFeed() {
  const videoRef = useRef(null);
  const [emotion, setEmotion] = useState("Detecting...");
  const [isCameraOn, setIsCameraOn] = useState(false);

  useEffect(() => {
    if (isCameraOn) {
      navigator.mediaDevices
        .getUserMedia({ video: true })
        .then((stream) => {
          if (videoRef.current) {
            videoRef.current.srcObject = stream;
          }

          // Start sending frames every second
          const interval = setInterval(() => captureFrameAndSend(), 1000);
          return () => clearInterval(interval);
        })
        .catch((error) => console.error("Error accessing webcam:", error));
    } else {
      if (videoRef.current && videoRef.current.srcObject) {
        let tracks = videoRef.current.srcObject.getTracks();
        tracks.forEach((track) => track.stop());
        videoRef.current.srcObject = null;
      }
    }
  }, [isCameraOn]);

  const captureFrameAndSend = async () => {
    if (!videoRef.current) return;

    const canvas = document.createElement("canvas");
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
        if (data.emotion) {
          setEmotion(data.emotion);
        } else {
          setEmotion("Error detecting emotion");
        }
      } catch (error) {
        console.error("Error sending frame:", error);
      }
    }, "image/jpeg");
  };

  return (
    <div className="flex flex-col items-center space-y-4 p-4">
      <video ref={videoRef} autoPlay className="w-96 h-auto rounded-lg shadow-md" />
      <button
        onClick={() => setIsCameraOn(!isCameraOn)}
        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
      >
        {isCameraOn ? "Turn Off Camera" : "Turn On Camera"}
      </button>
      <div className="text-xl font-bold mt-4">Emotion: {emotion}</div>
    </div>
  );
}
