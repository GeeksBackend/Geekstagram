from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.posts.models import Post, PostLike, PostComment
from apps.posts.serializers import PostSerializer, PostLikeSerializer, PostCommentSerializer

# Create your views here.
class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPI(CreateAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateAPI(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDestroyAPI(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#PostLike
class PostLikeCreateAPI(CreateAPIView):
    serializer_class = PostLikeSerializer

class PostLikeDestroyAPI(DestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

#PostComment
class PostCommentCreateAPI(CreateAPIView):
    serializer_class = PostCommentSerializer

class PostCommentUpdateAPI(UpdateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

class PostCommentDestroyAPI(DestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer