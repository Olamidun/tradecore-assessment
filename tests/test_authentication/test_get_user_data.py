import pytest
from rest_framework import status

@pytest.mark.django_db
class TestGetUserData:
    def test_successful_get_user_data(self, client, user_token):
        """
        
        Test for successful registration

        GIVEN: A user tries to get their data
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 200 and a json response containing their data

        """
        response = client.get("/api/v1/users/user", **user_token)
        response_data = response.json()
        
        assert response.status_code == 200
        assert isinstance(response_data, dict)