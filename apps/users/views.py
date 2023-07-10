from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from apps.users.models import User 
from apps.users.serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer

# Create your views here.
class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPI(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserRegisterAPI(CreateAPIView):
    serializer_class = UserRegisterSerializer