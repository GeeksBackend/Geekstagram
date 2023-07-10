from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.posts.models import Post 
from apps.posts.serializers import PostSerializer

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