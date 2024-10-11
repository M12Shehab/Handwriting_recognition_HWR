# -----------------------------------------------------------------------------
# Copyright (c) 2024 Mohammed A. Shehab
# All rights reserved.
#
# This software is licensed under the terms of the MIT license.
# For details, see the LICENSE file in the root directory of this distribution.
# -----------------------------------------------------------------------------
from locust import HttpUser, TaskSet, task, between

class InferenceTaskSet(TaskSet):
    @task
    def predict_digit(self):
        # Replace this payload with an example image payload as expected by your model
        payload = {"image": "<base64_encoded_image>"}
        self.client.post("/predict", json=payload)

class InferenceUser(HttpUser):
    tasks = [InferenceTaskSet]
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds between tasks

    # Define the host in the command line or here
    # host = "http://localhost:8000"
