from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Q
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer
from .permissions import IsOwnerOrReadOnly
from interactions.models import Follow  # Import Follow model

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'user__username']
    ordering_fields = ['created_at', 'likes_count', 'comments_count']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        # Annotate likes_count and comments_count
        queryset = Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comments', distinct=True)
        )
        return queryset

    @action(detail=False, methods=['get'])
    def my_posts(self, request):
        posts = self.get_queryset().filter(user=request.user)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def feed(self, request):
        # Get posts from users that the current user follows
        following_users = Follow.objects.filter(follower=request.user).values_list('following_id', flat=True)
        posts = self.get_queryset().filter(Q(user__in=following_users) | Q(user=request.user))
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)