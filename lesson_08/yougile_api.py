import requests


class YouGileAPI:
    BASE_URL = "https://yougile.com"

    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_project(self, title):
        # Нужен хотя бы один пользователь с ролью
        payload = {
            "title": title,
            "users": {
                "00084a63-6c19-40fe-9b40-85e0d2766bad": "admin"
            }
        }
        return requests.post(
            f"{self.BASE_URL}/projects",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id, new_title):
        return requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            json={"title": new_title},
            headers=self.headers
        )
