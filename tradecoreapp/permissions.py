from .models import Post
from rest_framework import permissions


class CanPerformActionOnPost(permissions.BasePermission):
    """
    Permission check if update and delete actions are about to be performed on posts

    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            print('Trueeeeeeeeeeeeeeeeee')
            return True
        print('Trueeeeeeeeeeeeeeeeee')
        return False