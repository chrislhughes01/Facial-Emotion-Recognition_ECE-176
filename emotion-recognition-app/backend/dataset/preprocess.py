import os
import numpy as np
import pandas as pd
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator

data_generator = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    brightness_range=[0.8, 1.2],
    shear_range=0.2
)

# Define paths
DATASET_DIR = "backend/dataset/dataset"
CSV_PATH = "backend/dataset/data.csv"
OUTPUT_FILE = "backend/dataset/processed_data.npz"

# Load CSV
df = pd.read_csv(CSV_PATH)

# Ensure correct column names
print("CSV Columns:", df.columns)  # Debugging step

if "path" not in df.columns or "label" not in df.columns:
    raise KeyError("CSV file is missing 'path' or 'label' columns.")

# Load and preprocess images
X = []
y = []
LABELS = df["label"].unique().tolist()  # Get unique labels
LABEL_MAP = {label: i for i, label in enumerate(LABELS)}

for _, row in df.iterrows():
    img_path = os.path.join(DATASET_DIR, row["path"])  # Construct full path

    if not os.path.exists(img_path):
        print(f"Warning: Image {img_path} not found, skipping.")
        continue

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (48, 48))
    img = img / 255.0  # Normalize

    X.append(img)
    y.append(LABEL_MAP[row["label"]])

X = np.array(X).reshape(-1, 48, 48, 1)
y = to_categorical(y, num_classes=len(LABELS))

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data
np.savez(OUTPUT_FILE, X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
print(f"Preprocessing complete! Saved as {OUTPUT_FILE}")
