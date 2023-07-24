from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPIView

router = DefaultRouter()
router.register('user', UserAPIView, 'api_users')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_login"),
    path('refresh/', TokenRefreshView.as_view(), name="api_refresh")
]

urlpatterns += router.urls