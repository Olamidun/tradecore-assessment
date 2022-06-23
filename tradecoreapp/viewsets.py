from ctypes.wintypes import PHKEY
from .models import Post
from rest_framework import status
from .services import PostManager
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from .permissions import CanPerformActionOnPost
from rest_framework.permissions import IsAuthenticated
from .serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer, PostUpdateSerializer

class PostViewSet(viewsets.ViewSet):
    """
    Viewset for Post CRUD
    """

    permission_classes = (IsAuthenticated, CanPerformActionOnPost)

    @swagger_auto_schema(
        operation_description="List out all posts",
        operation_summary="List posts",
        tags=["posts"],
    )
    def list(self, request):
        posts = PostManager.list_all_post()
        return Response(PostListSerializer(posts, many=True).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a posts",
        operation_summary="Create a posts",
        tags=["posts"]
    )
    def create(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        post = PostManager.create_post(user=request.user, **serializer.validated_data)
        return Response(PostCreateSerializer(post).data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        operation_description="Get a single post",
        operation_summary="Get post",
        tags=["posts"],
    )
    def retrieve(self, request, pk=None):
        post = PostManager.retrieve_single_post(pk)
        return Response(PostDetailSerializer(post).data, status=status.HTTP_200_OK)

    
    @swagger_auto_schema(
        request_body=PostUpdateSerializer,
        operation_description="Update a single post",
        operation_summary="Update post",
        tags=["posts"]
    )
    def partial_update(self, request, pk=None):
        post = PostManager.update_post(user=request.user, data=request.data, id=pk)
        return post

    
    @swagger_auto_schema(
        operation_description="Delete a single post",
        operation_summary="Delete post",
        tags=["posts"]
    )
    @action(detail=True, methods=['delete'], url_path="delete_post")
    def delete(self, request, pk):
        post = PostManager.delete_post(pk)
        return Response(post, status=status.HTTP_204_NO_CONTENT)

    
    @swagger_auto_schema(
        operation_description="Like a single post",
        operation_summary="Like post",
        tags=["posts"]
    )
    @action(detail=True, methods=['patch'], url_path="like_post")
    def like_post(self, request, pk):
        post = PostManager.like_post(request.user, pk)
        return Response(post, status=status.HTTP_200_OK)

    
    @swagger_auto_schema(
        operation_description="Unlike a single post",
        operation_summary="Unlike post",
        tags=["posts"]
    )
    @action(detail=True, methods=['patch'], url_path="unlike_post")
    def unlike_post(self, request, pk):
        post = PostManager.unlike_post(request.user, pk)
        return Response(post, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(
        operation_description="List out all posts for a user",
        operation_summary="List user posts",
        tags=["posts"]
    )
    @action(detail=False, methods=['get'], url_path="list_post_for_user")
    def list_posts_for_user(self, request):
        posts = PostManager.retrieve_all_user_post(request.user)
        return Response(PostListSerializer(posts, many=True).data, status=status.HTTP_200_OK)