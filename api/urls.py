from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, FollowViewSet

from .views import FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("", include(router.urls)),
]
