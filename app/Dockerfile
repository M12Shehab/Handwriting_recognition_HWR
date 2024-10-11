# Use an official TensorFlow image as the base
FROM tensorflow/tensorflow:latest
#LABEL authors="Shehab"

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the working directory
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY .. .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI server with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]