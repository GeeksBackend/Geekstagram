from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.posts.models import Post, PostLike, PostComment
from apps.posts.serializers import PostSerializer, PostLikeSerializer, PostCommentSerializer, PostDetailSerializer

# Create your views here.
class PostAPIView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer 
        return PostSerializer

#PostLike
class PostLikeAPIView(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

#PostComment
class PostCommentAPIView(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         GenericViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer