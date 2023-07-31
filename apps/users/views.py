from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.views import Response

from apps.users.models import User 
from apps.users.serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer
from apps.users.permissions import UserPermission

# Create your views here.
class UserAPIView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['username', 'email']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def get_serializer_class(self):
        print(self.action)
        if self.action in ('create', ):
            return UserRegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermission(), )
        return (AllowAny(), )
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'delete' : 'Пользователь успешно удален'}, status=status.HTTP_200_OK)
    
    # def create(self, request, *args, **kwargs):
    #     super().create(request, *args, **kwargs)
    #     return Response({'delete' : 'Пользователь успешно создан'}, status=status.HTTP_201_CREATED)