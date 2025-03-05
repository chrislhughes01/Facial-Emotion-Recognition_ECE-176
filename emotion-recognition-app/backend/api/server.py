from fastapi import FastAPI, File, UploadFile
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import uvicorn
import io
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS (Cross-Origin Requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change "*" to ["http://localhost:5173"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = load_model("backend/models/emotion_model.h5")

# Define emotion labels
EMOTIONS = ["Ahegao", "Angry", "Happy", "Neutral", "Sad", "Surprise"]

@app.post("/predict")
async def predict_emotion(file: UploadFile = File(...)):
    try:
        # Read image file
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("L")  # Convert to grayscale

        # Preprocess image
        image = image.resize((48, 48))  # Resize to model input size
        image = np.array(image) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)
        image = np.expand_dims(image, axis=-1)  # Add batch and channel dims

        # Make prediction
        predictions = model.predict(image)[0]
        emotion_index = np.argmax(predictions)
        emotion_label = EMOTIONS[emotion_index]

        # Prepare response with all probabilities
        emotion_probs = {EMOTIONS[i]: float(predictions[i]) for i in range(len(EMOTIONS))}

        return {
            "emotion": emotion_label,
            "confidence": float(predictions[emotion_index]),
            "probabilities": emotion_probs
        }

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
