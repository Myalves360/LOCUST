from locust import HttpUser, task, between

class ApiFakeUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")
    
    @task(2)  # A tarefa será executada com o dobro da frequência da anterior
    def outros_endpoints(self):
        self.client.get("/outro-endpoint")

