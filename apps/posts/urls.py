from rest_framework.routers import DefaultRouter

from apps.posts import views


router = DefaultRouter()
router.register('post', views.PostAPIView, "api_post")
router.register('like', views.PostLikeAPIView, "api_like")
router.register('comment', views.PostCommentAPIView, "api_comment")
router.register('favorite', views.PostFavoriteAPIVIew, "api_favorite")

urlpatterns = router.urls