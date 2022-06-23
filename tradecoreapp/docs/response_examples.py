from http.client import UNAUTHORIZED
from drf_yasg import openapi


UNAUTHORIZED = {
    "application/json": 
        {
            "detail": "Given token not valid for any token type",
            "code": "token_not_valid",
            "messages": [
                {
                    "token_class": "AccessToken",
                    "token_type": "access",
                    "message": "Token is invalid or expired"
                }
            ]
        }
}

NOT_FOUND = {
    "application/json": {"detail": "not found"}
}

BAD_REQUEST = {
    "application/json": {"content": ["This field is required"]}
}

SINGLE_POST_RESPONSE = {
    "application/json": {
        "id": 5,
        "content": "A new post",
        "liked_by": [
            1,
            2,
            3 # where these numbers are the ids of the users that liked the post
        ],
        "likes": 3,
        "user": "user@gmail.com"
    }
}

LIST_POST_RESPONSE = {
    "application/json": {
        "data": [
            {
                "id": 5,
                "content": "A new post",
                "liked_by": [
                    1,
                    2,
                    3 # where these numbers are the ids of the users that liked the post
                ],
                "likes": 3,
                "user": "user@gmail.com"
            },

            {
                "id": 6,
                "content": "Another Post",
                "liked_by": [
                    1,
                    3 # where these numbers are the ids of the users that liked the post
                ],
                "likes": 2,
                "user": "testuser@gmail.com"
            }
        ],
    }
}


LIKE_POST_RESPONSE = {
    "application/json": {
        "message": "post with id: 4 has been liked"
    }
}

UNLIKE_POST_RESPONSE = {
    "application/json": {
        "message": "post with id: 4 has been unliked"
    }
}


 
CREATE_POST = {
    201: openapi.Response(
        description="User created successfully",
        examples=SINGLE_POST_RESPONSE
    ),
    401: openapi.Response(
        description="Token is invalid or expired",
        examples=UNAUTHORIZED
    ),
    400: openapi.Response(
        description="Bad Request",
        examples=BAD_REQUEST
    )
}

LIST_POST = {
    200: openapi.Response(
        description="Posts fetched succesfully",
        examples=LIST_POST_RESPONSE
    )
}

GET_SINGLE_POST = {
    200: openapi.Response(
        description="Posts fetched succesfully",
        examples=SINGLE_POST_RESPONSE
    ),
    404: openapi.Response(
        description="Bad Request",
        examples=NOT_FOUND
    )
}


LIKE_SINGLE_POST = {
    200: openapi.Response(
        description="Post liked",
        examples=LIKE_POST_RESPONSE
    ),
    404: openapi.Response(
        description="Bad Request",
        examples=NOT_FOUND
    )
}

UNLIKE_SINGLE_POST = {
    200: openapi.Response(
        description="Posts fetched succesfully",
        examples=UNLIKE_POST_RESPONSE
    ),
    404: openapi.Response(
        description="Bad Request",
        examples=NOT_FOUND
    )
}