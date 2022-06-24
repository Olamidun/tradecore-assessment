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

USER_DATA_RESPONSE = {
    "application/json": {
        "id": 15,
        "email": "user@gmail.com",
        "is_superuser": False,
        "is_verified": False,
        "is_admin": False,
        "is_active": True,
        "is_staff": False,
        "date_joined": "2022-06-22T15:56:45.236932Z",
        "country": "United State of America",
        "city": "San Francisco",
        "continent": "North America",
        "region": "California",
        "name_of_holiday": None,
        "holiday_type": None,
        "holiday_date": None
    }
}


GET_USER_DATA = {
    200: openapi.Response(
        description="User fetched successfully",
        examples=USER_DATA_RESPONSE
    ),
    401: openapi.Response(
        description="Invalid API key",
        examples=UNAUTHORIZED
    )
}
