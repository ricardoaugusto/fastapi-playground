import os

from dotenv import load_dotenv
from fastapi import status
from fastapi.testclient import TestClient

from main import app

load_dotenv()
client = TestClient(app)


def create_test_user():
    client.post(
        "user",
        json={
            "name": "T1",
            "email": os.getenv("TEST_USER_EMAIL"),
            "password": os.getenv("TEST_USER_PASS"),
        },
    )


def get_access_token() -> str:
    # create_test_user()
    response = client.post(
        "/auth/token",
        data={
            "username": os.getenv("TEST_USER_EMAIL"),
            "password": os.getenv("TEST_USER_PASS"),
        },
    )

    return str(response.json().get("access_token"))


def test_get_notes_unauthorized():
    response = client.get("/note")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_get_notes():
    access_token = get_access_token()
    response = client.get(
        "/note",
        params={"page": 1, "per_page": 10},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == status.HTTP_200_OK
