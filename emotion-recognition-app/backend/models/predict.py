import tensorflow as tf
import numpy as np
import cv2
from tensorflow.keras.models import load_model

LABELS = ["Ahegao", "Angry", "Happy", "Neutral", "Sad", "Surprise"]

def predict_emotion(image_path):
    # Load the trained model
    model_path = "backend/models/emotion_model.h5"
    model = load_model(model_path)

    # Load image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (48, 48))
    image = image.reshape(1, 48, 48, 1) / 255.0  # Normalize

    # Predict
    prediction = model.predict(image)
    predicted_label = LABELS[np.argmax(prediction)]

    print(f"Predicted Emotion: {predicted_label}")

# Example usage
predict_emotion("backend/dataset/dataset/Happy/0a2c6596eca0d397fe67703fab598648dedec078a7e068601b1a632a.jpg")
