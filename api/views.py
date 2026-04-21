from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post, Group, Follow
from .serializers import PostSerializer, GroupSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission]
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username', 'user__username']
    
    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)