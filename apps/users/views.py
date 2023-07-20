from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.users.models import User 
from apps.users.serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer

# Create your views here.
class UserAPIView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        print(self.action)
        if self.action in ('create', ):
            return UserRegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer