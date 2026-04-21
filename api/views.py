from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from posts.models import Follow, Group, Post

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import FollowSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission]
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["group"]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["following__username", "user__username"]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
