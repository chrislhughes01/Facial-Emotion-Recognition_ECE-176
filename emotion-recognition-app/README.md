# Real-Time Facial Emotion Recognition Using a Webcam

## Overview
This project aims to develop a real-time facial emotion recognition system using a webcam. The system utilizes a convolutional neural network (CNN) to classify emotions and integrates with a frontend web application for real-time inference.

## Features
- Live webcam feed capturing
- Real-time emotion detection
- User-friendly web interface
- Flask-based backend with a pre-trained CNN model

## Project Structure
```
📂 emotion-recognition-app
├── 📂 frontend (React-based UI)
│   ├── 📂 src
│   │   ├── 📂 components (Reusable UI components)
│   │   ├── 📂 pages (Main application pages)
│   │   ├── 📂 styles (CSS files)
│   │   ├── 📄 App.jsx (Root component)
│   │   ├── 📄 main.jsx (Entry point)
│   ├── 📄 package.json (Dependencies & scripts)
│   ├── 📄 vite.config.js (Configuration for Vite)
├── 📂 backend (Flask API and CNN model)
│   ├── 📂 models (Pre-trained emotion recognition model)
│   ├── 📂 api (Flask endpoints for emotion detection)
│   ├── 📄 server.py (Main Flask app runner)
│   ├── 📄 requirements.txt (Backend dependencies)
├── 📄 README.md (Project documentation)
```

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/emotion-recognition-app.git
cd emotion-recognition-app
```

### 2. Setup the Backend
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python server.py
```

### 3. Setup the Frontend
```sh
cd frontend
npm install
npm run dev
```

## Usage
1. Start the backend (`python server.py`).
2. Start the frontend (`npm run dev`).
3. Open the browser and navigate to `http://localhost:5173`.
4. Click "Turn On Camera" and observe real-time emotion detection.

## Technologies Used
- **Frontend:** React, Vite
- **Backend:** Flask, TensorFlow, OpenCV
- **Model:** Pre-trained CNN for emotion recognition

## Future Enhancements
- Improve model accuracy with fine-tuning
- Deploy backend on cloud for broader accessibility
- Enhance UI with better visualization

## Contributors
- **Christopher Hughes (A16385527)**
- **Priscilla Nguyen (A16315357)**

## License
This project is licensed under the MIT License.

---

### Notes
- Ensure your webcam is properly connected and accessible in browser settings.
- If the model is not available, train and save it in `backend/models/emotion_model.h5`.

---
Let me know if you need any modifications or additional details! 🚀

