from locust import HttpUser, task, between

class ApiFakeUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_homepage(self):
        self.client.get("/")

    @task(3)
    def get_api(self):
        self.client.get("/api/fake")


