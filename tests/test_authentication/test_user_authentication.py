import pytest
from rest_framework import status

@pytest.mark.django_db
class TestAuthentication:
    def test_successful_user_registration(self, client):
        """
        
        Test for successful registration

        GIVEN: A user enters a valid email, and password
        WHEN: The user submits the form
        THEN: They should get a success response of status code 201, A message that says 'You account has been created successfully

        """
        data = {
            "email": "ajidi.amin@gmail.com",
            "password": "oyomesiogo"
        }

        response = client.post("/sellers/register", data=data)
        response_data = response.json()
        
        assert response.status_code == 201
        assert isinstance(response_data, dict)
        assert response_data["message"] == "Your account has been created successfully"

    @pytest.mark.parametrize(
        "registration_payload, expected_response",

        [
            (
                {},
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "email": [
                            "This field is required."
                        ],
                        "password": [
                            "This field is required."
                        ]
                    },
                ),
            ),
            (
                {
                    "email": "ajidi.amin@gmail.com",
                    "password": "oyoogo"
                },
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "password": [
                            "Ensure this field has at least 6 characters."
                        ]
                    },
                )
            ),
            (
                {
                    "email": "ajidi.amin@gmail.com",
                    "password": "oyoogovdsfvdsffdvdgfdgfbdfds"
                },
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "password": [
                            "Ensure this field has no more than 15 characters."
                        ]
                    },
                )
            ),

            (
                {
                    "email": "kolapoolamidunnnn@gmail.com",
                    "password": "oyoogovvdsddf"
                },
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "error": "This email could not be validated"
                    },
                )
            ),
        ],
    )
    def test_unsuccesful_user_registration(self, client, registration_payload, expected_response):
        """
        
        Test for unsuccessful registration

        GIVEN: A user enters a wrong details
        WHEN: The seller submits the form
        THEN: They should get a bad request response of status code 400, and a corresponding error message

        """
        response = client.post("/sellers/register", data=registration_payload)
        response_data = response.json()
        
        assert response.status_code == expected_response[0]
        assert response_data == expected_response[1]

    
    def test_user_registration_with_existing_email(self, user, register_user, client):
        """

        Test for registration with existing email address
        GIVEN: A seller attempts to register with an email that has already being used
        WHEN: Seller submits form
        THEN: They should get a bad request response of status code 400
        
        """
        data = {
            "email": register_user.email,
            "password": "oyomesiogo"
        }

        response = client.post("/api/v1/users/register", data=data)
        response_data = response.json()
        
        assert response.status_code == 400
        assert isinstance(response_data, dict)
        assert response_data["email"][0] == "user with this email already exists."

    def test_successful_login(self, register_user, client):
        """
        GIVEN: A user enters their email and password used when logging in
        WHEN: A user clicks on submit on the form
        THEN: The backend should return refresh and access tokens with status code of 200
        """

        data = {
            "email": register_user.email,
            "password": "mypassword123"
        }
        response = client.post("/api/v1/users/login", data=data)
        response_data = response.json()
        
        assert response.status_code == 200
        assert isinstance(response_data, dict)
        assert response_data["refresh"]
        assert response_data["access"]

    @pytest.mark.parametrize(
        "login_payload, expected_response",

        [
            (
                {},
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "email": [
                            "This field is required."
                        ],
                        "password": [
                            "This field is required."
                        ]
                    },
                ),
            ),
            (
                {
                    "email": "ajidi.amin@gmail.com",
                    "password": "oyoomesiogo"
                },
                (
                    status.HTTP_401_UNAUTHORIZED,
                    {
                        "detail": "No active account found with the given credentials"
                    },
                )
            )
        ],
    )
    def test_login_with_invalid_credentials(self, client, login_payload, expected_response):
        """
        GIVEN: A user enters their correct email and an invalid password
        WHEN: A user clicks on submit on the form
        THEN: The backend should return a 401 status code and an error message.
        """
        response = client.post("/api/v1/users/login", data=login_payload)
        response_data = response.json()
        
        assert response.status_code == expected_response[0]
        assert isinstance(response_data, dict)
        assert response_data == expected_response[1]


    def test_login_with_invalid_non_existent_email(self, register_user, client):
        data = {
            "email": "jhndoe@gmail.com",
            "password": "mypassword123"
        }
        response = client.post("/api/v1/users/login", data=data)
        response_data = response.json()
        
        assert response.status_code == 401
        assert isinstance(response_data, dict)
        assert response_data["detail"] == "No active account found with the given credentials"



    