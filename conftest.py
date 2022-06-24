import pytest
from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.fixture()
def register_user():
    user = User.objects.create_user(
        email="opeoluwakolapo@gmail.com",
    )
    user.set_password("mypassword123")
    user.save()
    return user

@pytest.fixture()
def user_token(register_user, client):
    response = client.post(
        '/api/v1/users/login', {
            "email": register_user.email, "password": "mypassword123"
        }
    )
    return {"HTTP_AUTHORIZATION": f"Bearer {response.json()['access']}", "Content-Type": "multipart/form-data"}

@pytest.fixture()
def invalid_user_token(register_user, client):
    response = client.post(
        '/api/v1/users/login', {
            "email": register_user.email, "password": "mypassword123"
        }
    )
    return {"HTTP_AUTHORIZATION": f"Bearer {response.json()['access']}cfgrty", "Content-Type": "multipart/form-data"}