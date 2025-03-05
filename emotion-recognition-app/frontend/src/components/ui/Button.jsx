export default function Button({ onClick, children }) {
  return (
    <button
      onClick={onClick}
      className="mt-4 px-6 py-3 bg-blue-600 text-white text-lg font-semibold rounded-lg 
                 hover:bg-blue-700 transition-all duration-200 shadow-lg 
                 focus:ring-2 focus:ring-blue-400 focus:outline-none"
    >
      {children}
    </button>
  );
}
