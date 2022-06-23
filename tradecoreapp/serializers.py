from .models import Post
from rest_framework import serializers


class PostCreateSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    def create(self, validated_data):
        content = validated_data.get('content')
        post = Post.objects.create(content=content)
        return post


class PostListSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField('number_of_likes')
    user = serializers.SerializerMethodField('post_author')
    
    class Meta:
        model = Post
        fields = ['content', 'user', 'likes']

    def post_author(self, post):
        user = post.user.email
        return user

    def number_of_likes(self, post):
        return post.likes


class PostDetailSerializer(serializers.ModelSerializer):
    liked_by = serializers.SerializerMethodField('liked_by')
    likes = serializers.SerializerMethodField('number_of_likes')
    user = serializers.SerializerMethodField('post_author')
    
    class Meta:
        model = Post
        fields = ['content', 'liked_by', 'likes', 'user']

    def post_author(self, post):
        user = post.user.email
        return user
    
    def liked_by(self, post):
        return post.liked_by.all()

    def number_of_likes(self, post):
        return post.likes


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content']