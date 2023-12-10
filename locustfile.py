from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def task1(self):
        self.client.get("/")