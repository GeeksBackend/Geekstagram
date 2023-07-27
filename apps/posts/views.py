from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.posts.models import Post, PostLike, PostComment, PostFavorite
from apps.posts.serializers import PostSerializer, PostLikeSerializer, PostCommentSerializer, PostDetailSerializer, PostCreateSerializer, PostFavoriteSerializer
from apps.posts.permissions import PostPermission

# Create your views here.
class PostAPIView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated, )

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer 
        if self.action == "create":
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

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

#PostFavorite
class PostFavoriteAPIVIew(mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    queryset = PostFavorite.objects.all()
    serializer_class = PostFavoriteSerializer
    permission_classes = (PostPermission, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return PostFavorite.objects.filter(user=self.request.user)