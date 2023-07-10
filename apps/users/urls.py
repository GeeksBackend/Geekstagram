from django.urls import path 

from apps.users.views import UserAPI, UserRetrieveAPI, UserRegisterAPI

urlpatterns = [
    path('', UserAPI.as_view(), name='api_users'),
    path('<int:pk>/', UserRetrieveAPI.as_view(), name='api_users_retrieve'),
    path('create/', UserRegisterAPI.as_view(), name='api_users_register')
]