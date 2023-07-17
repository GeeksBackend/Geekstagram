from django.urls import path

from apps.posts.views import PostAPIView, PostRetrieveAPI, PostCreateAPI, PostUpdateAPI, PostDestroyAPI, PostLikeCreateAPI, PostLikeDestroyAPI, PostCommentCreateAPI, PostCommentUpdateAPI, PostCommentDestroyAPI

urlpatterns = [
    path('', PostAPIView.as_view(), name="api_posts"),
    path('<int:pk>/', PostRetrieveAPI.as_view(), name="api_retrieve_post"),
    path('create/', PostCreateAPI.as_view(), name="api_create_post"),
    path('update/<int:pk>/', PostUpdateAPI.as_view(), name="api_update_post"),
    path('destroy/<int:pk>/', PostDestroyAPI.as_view(), name="api_destroy_post"),
    path('like/create/', PostLikeCreateAPI.as_view(), name="api_create_like"),
    path('like/destroy/<int:pk>/', PostLikeDestroyAPI.as_view(), name='api_destroy_like'),
    path('comment/create/', PostCommentCreateAPI.as_view(), name="api_create_comment"),
    path('comment/update/<int:pk>/', PostCommentUpdateAPI.as_view(), name="api_comment_update"),
    path('comment/destroy/<int:pk>/', PostCommentDestroyAPI.as_view(), name="api_comment_destroy")
]