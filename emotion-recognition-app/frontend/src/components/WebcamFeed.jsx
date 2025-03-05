import { useRef, useEffect, useState } from "react";
import Button from "./ui/Button";

export default function WebcamFeed() {
  const videoRef = useRef(null);
  const [isCameraOn, setIsCameraOn] = useState(false);

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
        const stream = videoRef.current.srcObject;
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        videoRef.current.srcObject = null;
      }
    }
  }, [isCameraOn]);

  return (
    <div className="flex flex-col items-center justify-center w-full">
      <div className="bg-gray-800 rounded-lg shadow-lg p-6 flex flex-col items-center w-full max-w-lg">
        <div className="flex flex-col items-center justify-center w-full">
          {isCameraOn ? (
            <video
              ref={videoRef}
              autoPlay
              className="w-[500px] h-auto rounded-lg shadow-lg border-4 border-blue-500"
            />
          ) : (
            <div className="w-[500px] h-[375px] bg-gray-700 rounded-lg flex items-center justify-center">
              <p className="text-gray-400">Camera is off</p>
            </div>
          )}

          {/* Wrapping button inside a flex container */}
          <div className="mt-4 flex justify-center w-full">
            <Button onClick={() => setIsCameraOn(!isCameraOn)}>
              {isCameraOn ? "Turn Off Camera" : "Turn On Camera"}
            </Button>
          </div>
        </div>
      </div>

      <p className="text-gray-400 mt-6 text-center text-sm">
        The emotion recognition model will analyze your expressions in real-time.
      </p>
    </div>
  );
}
