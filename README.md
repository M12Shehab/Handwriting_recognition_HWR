# MNIST Handwritten Digits Classification and Inference Server

## Overview
This project, developed by Mohammed Shehab, presents a neural network training pipeline for classifying MNIST handwritten digits using TensorFlow/Keras. The project includes building and tuning a Convolutional Neural Network (CNN) model within a Jupyter notebook, followed by deploying the trained model as an inference server using Docker containerization with FastAPI.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Deployment](#model-deployment)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features
- Data loading and preprocessing for MNIST digit classification
- Construction and hyperparameter tuning of a CNN model for MNIST
- Exporting the optimized model for deployment
- FastAPI-based inference server deployment using Docker

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/M12Shehab/Handwriting_recognition_HWR.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Handwriting_recognition_HWR
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Jupyter Notebook**:
   Open the Jupyter notebook to load data, build, and tune the CNN model.
   ```bash
   jupyter notebook Model_Devlopment.ipynb
   ```

2. **Run Tests with Pytest**:
   Ensure the code is functioning as expected by running tests:
   ```bash
   pytest tests
   ```
   _Note: The tests are located in the `tests` directory. Also, you need to run the FastAPI server before running the tests._

## Model Deployment
1. **Build the Docker Image**:
   ```bash
   docker build -t fastapi-mnist-app .
   ```
2. **Run the Docker Container**:
   ```bash
   docker run -p 8000:8000 fastapi-mnist-app
   ```
   This will start the FastAPI server, accessible at `http://localhost:8000`.

## Technologies Used
- Python
- TensorFlow/Keras for CNN model development and tuning
- Jupyter Notebook for model training
- FastAPI for serving the model as an inference server
- Docker for containerization
- Pytest for testing

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for any improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
