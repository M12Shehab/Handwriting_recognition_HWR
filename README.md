# MNIST Handwritten Digits Classification and Inference Server

## Overview
This project, developed by Mohammed Shehab, presents a neural network training pipeline for classifying MNIST handwritten digits using TensorFlow/Keras. The project includes building and tuning a Convolutional Neural Network (CNN) model within a Jupyter notebook, followed by deploying the trained model as an inference server using Docker containerization with FastAPI.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Deployment](#model-deployment)
- [Performance Testing with Locust](#performance-testing-with-locust)
- [Experiment Tracking with MLflow](#experiment-tracking-with-mlflow)
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

## Performance Testing with Locust
You can use Locust to test the performance of the FastAPI inference server:

1. **Install Locust**:
   ```bash
   pip install locust
   ```

2. **Run the Locust Test**:
   ```bash
   cd tests
   locust -f locustfile.py --host=http://localhost:8000
   ```
   Open your browser and go to `http://localhost:8089`. Enter the number of users and spawn rate to simulate load on the server. Locust will provide insights into response times, throughput, and error rates.

## Experiment Tracking with MLflow
MLflow is used to track training experiments, hyperparameters, and model artifacts within this project.

1. **Install MLflow** (if not already installed):
   ```bash
   pip install mlflow
   ```

2. **Run the Jupyter Notebook with MLflow Tracking**:
   - MLflow automatically logs model parameters, metrics, and artifacts during training in the notebook.
   - To track experiments, simply execute the notebook cells. MLflow will start logging runs automatically.

3. **View MLflow Experiment Logs**:
   - Launch the MLflow UI to explore your experiment logs and model artifacts:
     ```bash
     mlflow ui
     ```
   - Open your browser and go to `http://localhost:5000` to access the MLflow dashboard.

4. **Check MLflow Logs for Parameters and Metrics**:
   - Within the MLflow UI, you can view detailed metrics such as accuracy and hyperparameters logged for each training run. The model can also be downloaded for deployment from the UI.

## Technologies Used
- Python
- TensorFlow/Keras for CNN model development and tuning
- Jupyter Notebook for model training
- FastAPI for serving the model as an inference server
- Docker for containerization
- Pytest for testing
- Locust for performance testing
- MLflow for experiment tracking

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for any improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

