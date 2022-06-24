import pytest
from rest_framework import status

@pytest.mark.django_db
class TestGetUserData:
    def test_successful_get_user_data(self, client, user_token):
        """
        
        Test for successful retieval of user data

        GIVEN: A user tries to get their data
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 200 and a json response containing their data

        """
        response = client.get("/api/v1/users/user", **user_token)
        response_data = response.json()
        
        assert response.status_code == 200
        assert isinstance(response_data, dict)

    def test_unsuccessful_get_user_data_invalid_token(self, client, invalid_user_token):
        """
        
        Test for unsuccessful retieval of user data

        GIVEN: A user tries to get their data
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 401 and an error message

        """
        response = client.get("/api/v1/users/user", **invalid_user_token)
        response_data = response.json()
        
        assert response.status_code == 401
        assert response.json()["detail"] == "Given token not valid for any token type"
        assert response.json()["code"] == "token_not_valid"
        assert response.json()["messages"][0]["message"] == "Token is invalid or expired"

    def test_unsuccessful_get_user_data_no_token(self, client, user_token):
        """
        
        Test for unsuccessful retieval of user data

        GIVEN: A user tries to get their data
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 401 and an error message

        """
        response = client.get("/api/v1/users/user")
        response_data = response.json()
        
        assert response.status_code == 401
        assert response.json()['detail'] == "Authentication credentials were not provided."