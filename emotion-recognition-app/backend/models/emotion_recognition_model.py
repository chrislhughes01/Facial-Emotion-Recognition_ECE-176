import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import AdamW
from tensorflow.keras.applications import MobileNetV2

def build_emotion_recognition_model():
    base_model = MobileNetV2(input_shape=(48, 48, 3), include_top=False, weights="imagenet")
    base_model.trainable = False  # Freeze pretrained layers

    model = Sequential([
        base_model,
        Flatten(),
        Dense(512, activation="relu"),
        Dropout(0.4),
        Dense(6, activation="softmax")  # Output layer
    ])

    # Compile model
    model.compile(optimizer=Adam(learning_rate=0.0001), loss="categorical_crossentropy", metrics=["accuracy"])
    model.save("backend/models/emotion_recognition_model.h5")
    return model
    """
    model = Sequential()
    
    # First Conv Block
    model.add(Conv2D(64, (3,3), activation='linear', padding='same', input_shape=(48, 48, 1)))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    # Second Conv Block
    model.add(Conv2D(128, (3,3), activation='linear', padding='same'))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    # Third Conv Block
    model.add(Conv2D(256, (3,3), activation='linear', padding='same'))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    # Flatten and Dense Layers
    model.add(Flatten())
    model.add(Dense(512, activation='linear'))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
    model.add(Dropout(0.5))
    
    # Output Layer
    model.add(Dense(6, activation='softmax'))
    
    # Compile Model with AdamW Optimizer
    model.compile(loss='categorical_crossentropy', optimizer=AdamW(learning_rate=0.001, weight_decay=1e-5), metrics=['accuracy'])
    
    return model
    """
