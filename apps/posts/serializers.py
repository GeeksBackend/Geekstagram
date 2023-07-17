from rest_framework import serializers

from apps.posts.models import Post, PostLike, PostComment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike 
        fields = ('id', 'user', 'post')

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ('id', 'user', 'post', 'text', 'created')