import pytest
from rest_framework import status

@pytest.mark.django_db
class TestCreatePost:
    def test_succesful_post_create(self, client, user_token):
        """
        Test for successful post creation

        GIVEN: A user enters text-based content of a post
        WHEN: The user submits the form
        THEN: They should get a success response of status code 201, and a response containing the post content and id'
        """
        data = {
            "content": "This is a new post for testing..."
        }

        response = client.post("/api/v1/post", data=data, **user_token)
        response_data = response.json()
        assert response.status_code == 201

    def test_create_post_with_invalid_token(self, client, invalid_user_token):
        """
        Test for unsuccessful post creation due to invalid token

        GIVEN: A user enters text-based content of a post
        WHEN: The user submits the form but is using an invalid token
        THEN: They should get a success response of status code 401, and a response containing the post content and id'
        """
        data = {
            "content": "This is a new post for testing..."
        }

        response = client.post("/api/v1/post", data=data, **invalid_user_token)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["detail"] == "Given token not valid for any token type"
        assert response_data["code"] == "token_not_valid"
        assert response_data["messages"][0]["message"] == "Token is invalid or expired"

    def test_create_post_with_no_token(self, client, user_tokan):
        """
        Test for unsuccessful post creation due to no token

        GIVEN: A user enters text-based content correctly but is not authenticated
        WHEN: The seller submits the form
        THEN: They should get a success response of status code 401, A message that tells them that they are have no provided authentication credentials
        
        """
        esponse = client.post("/api/v1/post", data=data)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["detail"] == "Authentication credentials were not provided."

    @pytest.mark.parametrize(
        "post_payload, expected_response",
        [
            (
                {},
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "content": [
                            "This field is required."
                        ]
                    },
                ),
            )
        ],
    )

    def test_create_item_unsuccessful(self, client, user_token, post_payload, expected_response):
        """
        Test for unsuccessful post creation
        GIVEN: A user does not enter the content field
        WHEN: The user submits the form
        THEN: They should get a bad request response of status code 400
        
        """

        response = client.post("/items/create_item", data=item_payload, **seller_token)
        response_data = response.json()

        assert response.status_code == expected_response[0]
        assert response_data == expected_response[1]