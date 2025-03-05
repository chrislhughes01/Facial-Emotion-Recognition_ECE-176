import WebcamFeed from "../components/WebcamFeed.jsx";

export default function Home() {
  return (
    <div className="flex flex-col items-center min-h-screen p-4">
      <h1 className="text-2xl font-bold">Real-Time Emotion Recognition</h1>
      <WebcamFeed />
    </div>
  );
}