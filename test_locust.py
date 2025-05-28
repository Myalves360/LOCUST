from locust import HttpUser, task, between

class UsuarioSimulado(HttpUser):
    wait_time = between(1, 3)
    host = "https://reqres.in"  # <- API pública que funciona

    @task
    def acessar_usuarios(self):
        self.client.get("/api/users")  # endpoint que existe


