from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "account"

urlpatterns = [
    path('register', views.RegistrationAPIView.as_view(), name='register'),
    path('login', views.LoginWithEmailView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('user', views.GetUserDataAPIView.as_view(), name="user_data")
]