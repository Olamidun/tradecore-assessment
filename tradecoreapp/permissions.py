from .models import Post
from rest_framework import permissions


class CanPerformActionOnPost(permissions.BasePermission):
    """
    Permission check if update and delete actions are about to be performed on posts

    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user