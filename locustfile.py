from locust import HttpUser, task


class WebsiteUser(HttpUser):

    @task
    def task1(self):
        self.client.get("/")