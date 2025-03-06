import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, LeakyReLU
from tensorflow.keras.optimizers import Adam

# Load the processed dataset
data = np.load("backend/dataset/processed_data.npz", allow_pickle=True)
X_train, y_train = data["X_train"], data["y_train"]
class_weights = data["class_weights"].item()  # Convert to dictionary

# Define the CNN Model
model = Sequential([
    Conv2D(64, (3, 3), padding="same", input_shape=(48, 48, 1)),
    BatchNormalization(),
    LeakyReLU(),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), padding="same"),
    BatchNormalization(),
    LeakyReLU(),
    MaxPooling2D((2, 2)),

    Conv2D(256, (3, 3), padding="same"),
    BatchNormalization(),
    LeakyReLU(),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(512),
    BatchNormalization(),
    LeakyReLU(),
    Dropout(0.4),

    Dense(y_train.shape[1], activation="softmax")  # Output layer
])

# Compile the model
opt = Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])

# Train the model using class weights
model.fit(X_train, y_train, epochs=50, batch_size=64, validation_split=0.2, class_weight=class_weights)

# Save the improved model
model.save("backend/models/emotion_recognition_model.h5")
