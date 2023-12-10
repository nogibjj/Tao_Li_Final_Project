from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_grocery_info(self):
        self.client.get("/grocery_info/coffee")

    @task
    def load_count_info(self):
        self.client.get("/product_count/20")