import { useRef, useEffect, useState } from "react";
import { Button } from "@/components/ui/button";

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
    <div className="flex flex-col items-center space-y-4 p-4">
      <video ref={videoRef} autoPlay className="w-96 h-auto rounded-lg shadow-md" />
      <Button onClick={() => setIsCameraOn(!isCameraOn)}>
        {isCameraOn ? "Turn Off Camera" : "Turn On Camera"}
      </Button>
    </div>
  );
}
