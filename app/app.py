# -----------------------------------------------------------------------------
# Copyright (c) 2024 Mohammed A. Shehab
# All rights reserved.
#
# This software is licensed under the terms of the MIT license.
# For details, see the LICENSE file in the root directory of this distribution.
# -----------------------------------------------------------------------------
# This file contains the FastAPI application that loads the trained model and serves predictions.
import logging
import time
from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MODEL_VERSION = "v1_0_1"
model_directory = f'best_model_{MODEL_VERSION}.h5'
# Try loading the model and log the outcome
# Try loading the model and log the outcome
try:
    model = load_model(model_directory)
    logging.info("Model version %s loaded successfully from %s.", MODEL_VERSION, model_directory)
except Exception as e:
    logging.error("Failed to load model version %s from %s. Error: %s", MODEL_VERSION, model_directory, e)
    raise
print("Model loaded successfully")

app = FastAPI()

# define the API routes
@app.get("/")
def home():
    return {"health_check": "OK",
            "model_version": MODEL_VERSION,
            "model_name": "MNIST Classifier",
            "Deployed by": "Mohammed A. Shehab"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    start_time = time.time()  # Start timing

    # Load and preprocess the image
    image = Image.open(io.BytesIO(await file.read())).convert('L').resize((28, 28))
    image = np.array(image).reshape(1, 28, 28, 1) / 255.0  # Normalize

    # Make prediction
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    confidence = float(np.max(prediction))

    # Calculate and log the prediction time
    prediction_time = time.time() - start_time
    logging.info("Prediction time: %.4f seconds for model version %s", prediction_time, MODEL_VERSION)

    # Return the prediction, confidence, and prediction time
    return {"class": int(predicted_class), "confidence": confidence, "prediction_time": prediction_time}
