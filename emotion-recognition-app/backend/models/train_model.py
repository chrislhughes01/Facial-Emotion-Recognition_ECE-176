import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from emotion_recognition_model import create_emotion_model
import os

# Load the preprocessed dataset
dataset_path = "backend/dataset/processed_data.npz"
data = np.load(dataset_path)

X_train, y_train = data["X_train"], data["y_train"]
X_test, y_test = data["X_test"], data["y_test"]

# Create the model
model = create_emotion_model()

# Train the model
EPOCHS = 25
BATCH_SIZE = 64

history = model.fit(X_train, y_train, validation_data=(X_test, y_test),
                    batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=1)

# Save the trained model
model_save_path = "backend/models/emotion_model.h5"
model.save(model_save_path)

print(f"✅ Model training complete! Saved as {model_save_path}")
