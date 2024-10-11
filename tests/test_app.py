import pytest
import requests
from PIL import Image
import numpy as np
import os

# Define the FastAPI app URL
BASE_URL = "http://localhost:8000/"

# Helper function to create a mock MNIST-like image
def create_test_image():
    image = Image.new('L', (28, 28), color=255)
    pixels = image.load()
    for i in range(10, 20):
        pixels[i, 14] = 0
    for i in range(14, 18):
        pixels[20, i] = 0
    for i in range(20, 26):
        pixels[i, 18] = 0
    image_bytes = np.array(image)
    return image_bytes


# Test the / endpoint (health check)
def test_home():
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200
    response_json = response.json()

    # Check that the response contains expected keys and values
    assert response_json["health_check"] == "OK"
    assert "model_version" in response_json
    assert "Deployed by" in response_json
    assert response_json["model_name"] == "MNIST Classifier"
    assert response_json["Deployed by"] == "Mohammed A. Shehab"

# Test the /predict endpoint on localhost
def test_predict():
    # Create an in-memory image
    image_data = create_test_image()
    image = Image.fromarray(image_data).convert("L")
    test_image_path = os.path.join("./", "test_digit.png")
    image.save(test_image_path, format="PNG")

    # Open and read the image file, then send it as part of the request to the API
    with open(test_image_path, "rb") as f:
        files = {"file": ("test_digit.png", f, "image/png")}
        response = requests.post(BASE_URL+"/predict", files=files)

    # Assert the response is successful and contains required keys
    assert response.status_code == 200
    response_json = response.json()
    assert "class" in response_json
    assert "confidence" in response_json
    assert isinstance(response_json["class"], int)
    assert isinstance(response_json["confidence"], float)

# Clean up after tests
@pytest.fixture(scope="module", autouse=True)
def cleanup():
    yield
    test_image_path = os.path.join("./", "test_digit.png")
    if os.path.exists(test_image_path):
        os.remove(test_image_path)
