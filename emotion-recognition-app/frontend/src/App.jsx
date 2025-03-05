import WebcamFeed from "./components/WebcamFeed";

export default function App() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-6 text-center">
        Real-Time Emotion Recognition
      </h1>
      <WebcamFeed />
    </div>
  );
}