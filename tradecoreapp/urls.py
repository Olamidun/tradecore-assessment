from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

app_name = "tradecoreapp"
router = DefaultRouter()

router.register(r"post", viewsets.PostViewSet, basename="post-viewset")


urlpatterns = [
    path("", include(router.urls)),
]

