import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report
from tensorflow.keras.models import load_model

# Load preprocessed dataset
dataset_path = "backend/dataset/processed_data.npz"
data = np.load(dataset_path)

X_test, y_test = data["X_test"], data["y_test"]

# Load trained model
model_path = "backend/models/emotion_model.h5"
model = load_model(model_path)
model.summary()

# Evaluate performance
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

report = classification_report(y_true_classes, y_pred_classes, target_names=["Ahegao", "Angry", "Happy", "Neutral", "Sad", "Surprise"])
print(report)
