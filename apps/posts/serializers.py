from rest_framework import serializers

from apps.posts.models import Post, PostLike, PostComment, PostFavorite


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'image', 'created')

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike 
        fields = ('id', 'user', 'post')

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ('id', 'user', 'post', 'text', 'created')

class PostDetailSerializer(serializers.ModelSerializer):
    #comment
    post_comments = PostCommentSerializer(read_only=True, many=True)
    count_comments = serializers.SerializerMethodField(read_only=True)
    #like
    post_likes = PostLikeSerializer(read_only=True, many=True)
    count_likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 
                  'image', 'created', 'user',
                  'post_comments', 'post_likes',
                  'count_comments', 'count_likes')
        
    def get_count_comments(self, obj):
        return obj.post_comments.all().count()
    
    def get_count_likes(self, obj):
        return obj.post_likes.all().count()

class PostFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFavorite
        fields = ('id', 'post')