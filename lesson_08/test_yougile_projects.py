import requests
from yougile_api import YouGileAPI

# === Настройки ===
TOKEN = ""  # ← замени на свой
BASE_URL = "https://yougile.com/api-v2"
api = YouGileAPI(TOKEN)


# --- CREATE ---
def test_create_project_positive():
    resp = api.create_project("Проект через PageObject")
    assert resp.status_code == 201

    data = resp.json()
    assert "id" in data  # ← проверяем, что есть id
    project_id = data["id"]
    # Получаем проект по ID — там будет title
    resp_get = api.get_project(project_id)
    assert resp_get.status_code == 200
    created_data = resp_get.json()
    assert created_data["title"] == "Проект через PageObject"
    assert created_data["id"] == project_id


def test_create_project_negative_missing_title():
    resp = requests.post(
        BASE_URL + "/projects",
        json={},
        headers=api.headers
    )
    assert resp.status_code == 400


# --- GET ---
def test_get_project_positive():
    create_resp = api.create_project("Временный проект")
    project_id = create_resp.json()["id"]

    resp = api.get_project(project_id)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Временный проект"


def test_get_project_negative_invalid_id():
    resp = api.get_project("999999999")
    assert resp.status_code == 404


# --- UPDATE ---
def test_update_project_positive():
    # Создаём проект
    create_resp = api.create_project("Было")
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]
    # Обновляем
    update_resp = api.update_project(project_id, "Стало")
    assert update_resp.status_code == 200
    # Получаем обновлённый проект
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    data = get_resp.json()

    assert data["title"] == "Стало"


def test_update_project_negative_invalid_id():
    # Пытаемся обновить проект с несуществующим ID
    invalid_id = "00000000-0000-0000-0000-000000000000"
    update_resp = api.update_project(invalid_id, "Новое название")
    # Ожидаем ошибку 404 (Not Found)
    assert update_resp.status_code == 404
