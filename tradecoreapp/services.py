from .models import Post
from django.db.models import F
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from tradecoreapp.serializers import PostUpdateSerializer

class PostManager:
    """
    Manager class to manage post CRUD
    """

    @classmethod
    def create_post(cls, user, **kwargs):
        return Post.objects.create(user=user, **kwargs)

    @classmethod
    def list_all_post(cls):
        return Post.objects.select_related("user").all()

    @classmethod
    def retrieve_single_post(cls, id):
        try:
            post = Post.objects.select_related("user").prefetch_related("liked_by").get(id=id)
            return post
        except Post.DoesNotExist as e:
            raise Http404 from e
    
    @classmethod
    def retrieve_all_user_post(cls, user):
        return Post.objects.select_related('user').filter(user=user)

    @classmethod
    def update_post(cls, data, user, id):
        post = cls.retrieve_single_post(id)
        serialized_data = PostUpdateSerializer(post, data, partial=True)
        if not serialized_data.is_valid():
            raise ValidationError({"errors": serialized_data.errors}, code=status.HTTP_400_BAD_REQUEST)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    @classmethod
    def delete_post(cls, id):
        post = cls.retrieve_single_post(id)
        post.delete()
        return {"message": "Post has been deleted successfully"}

    @classmethod
    def like_post(cls, user, id):
        post = cls.retrieve_single_post(id)
        post.likes = F('likes') + 1
        post.liked_by.add(user)
        post.save()
        return {"message": f"Post with id: {id} has been liked"}
    
    @classmethod
    def unlike_post(cls, user, id):
        post = cls.retrieve_single_post(id)
        post.likes = F('likes') - 1
        post.liked_by.remove(user)
        post.save()
        return {"message": f"Post with id: {id} has been unliked"}



    