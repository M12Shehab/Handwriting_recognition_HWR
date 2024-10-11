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
        files = {
            'file': ('test_image4kB.png', open('test_image4kB.png', 'rb'), 'image/png')
        }
        with self.client.post("/predict", files=files, catch_response=True) as response:
            if response.status_code == 200:
                print("Success:", response.json())
            else:
                print("Failed:", response.status_code, response.text)


class InferenceUser(HttpUser):
    tasks = [InferenceTaskSet]
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds between tasks

    # Define the host in the command line or here
    # host = "http://localhost:8000"
