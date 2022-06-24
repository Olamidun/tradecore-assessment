import pytest
from rest_framework import status

@pytest.mark.django_db
class TestGetPost:
    def test_successful_get_list_of_posts(self, client, user_token):
        """
        Test for successful post creation

        GIVEN: A user tries to view other posts
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 200, and list of posts in json format
        """

        response = client.get('api/v1/post', client, user_token)
        assert response.status_code == 200
        assert isinstance(response.json(), list) is True

    
    def test_unsuccessful_get_list_of_posts_no_token(self, client, user_token):
        """
        Test for unsuccessful list of posts retrieval
        GIVEN: A user tries to view other posts without being authenticated
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 401, and an error message that says "Authentication credentials were not provided
        """

        response = client.get('api/v1/post', client)
        assert response.status_code == 401
        assert response.json()['detail'] == "Authentication credentials were not provided."

    def test_unsuccessful_get_list_of_posts_invalid_token(self, client, invalid_user_token):
        """
        Test for unsuccessful list of posts retrieval

        GIVEN: A user tries to view other posts with expired or invalid token
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 401, and an error message that says "Authentication credentials were not provided
        """

        response = client.get('api/v1/post', client, **invalid_user_token)
        assert response.status_code == 401
        assert response.json()["detail"] == "Given token not valid for any token type"
        assert response.json()["code"] == "token_not_valid"
        assert response.json()["messages"][0]["message"] == "Token is invalid or expired"

    
    def test_successful_get_list_of_user_posts(self, client, user_token):
        """
        Test for successful list of user posts retrieval

        GIVEN: A user tries to view all the posts they have created
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 200, and list of posts in json format
        """

        response = client.get('api/v1/post/list_post_for_user', client, user_token)
        assert response.status_code == 200
        assert isinstance(response.json(), list) is True

    
    def test_unsuccessful_get_list_of_user_posts_no_token(self, client, user_token):
        """
        Test for unsuccessful list of user posts retrieval

        GIVEN: A user tries to view all they posts they have created without being authenticated
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 401, and an error message that says "Authentication credentials were not provided
        """

        response = client.get('api/v1/post/list_post_for_user', client)
        assert response.status_code == 401
        assert response.json()['detail'] == "Authentication credentials were not provided."

    
    def test_unsuccessful_get_list_of_user_posts_invalid_token(self, client, invalid_user_token):
        """
        Test for unsuccessful list of user posts retrieval

        GIVEN: A user tries to view the posts they have created with expired or invalid token
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 401.
        """

        response = client.get('api/v1/post/list_post_for_user', client, **invalid_user_token)
        assert response.status_code == 401
        assert response.json()["detail"] == "Given token not valid for any token type"
        assert response.json()["code"] == "token_not_valid"
        assert response.json()["messages"][0]["message"] == "Token is invalid or expired"

    def test_retrieve_single_post_successful(self, client, user_token):
        """
        Test for successful single post retrieval

        GIVEN: A user tries to view a single post
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 200
        """

        post = Post.objects.create(content="a single post")

        response = client.get(f'api/v1/post/{post.id}', client, **user_token)
        assert response.status_code == 200

    def test_retrieve_single_post_unsuccessful_invalid_token(self, client, **invalid_user_token):
        """
        Test for unsuccessful single post retrieval

        GIVEN: A user tries to view a single post but they are unauthenticated.
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 200
        """

        post = Post.objects.create(content="a single post")

        response = client.get(f'api/v1/post/{post.id}', client, **invalid_user_token)
        assert response.status_code == 401
        assert response.json()["detail"] == "Given token not valid for any token type"
        assert response.json()["code"] == "token_not_valid"
        assert response.json()["messages"][0]["message"] == "Token is invalid or expired"

    
    def test_retrieve_single_post_unsuccessful_no_token(self, client, **invalid_user_token):
        """
        Test for unsuccessful single post retrieval

        GIVEN: A user tries to view a single post but with an invalid or expired token.
        WHEN: The user hits the endpoint
        THEN: They should get a success response of status code 200
        """

        post = Post.objects.create(content="a single post")

        response = client.get(f'api/v1/post/{post.id}', client)
        assert response.status_code == 401
        assert response.json()["detail"] == "Given token not valid for any token type"
        assert response.json()["code"] == "token_not_valid"
        assert response.json()["messages"][0]["message"] == "Token is invalid or expired"
