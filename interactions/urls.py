from django.urls import path, include  # 'include' is used below for including router URLs
from rest_framework.routers import DefaultRouter
from .views import (
    CommentViewSet, 
    LikeViewSet, 
    FollowViewSet,
    FollowersListView,
    FollowingListView
)

comment_router = DefaultRouter()
comment_router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('posts/<int:post_id>/', include(comment_router.urls)),
    path('posts/<int:post_id>/like/', LikeViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:post_id>/unlike/', LikeViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
    path('users/<int:user_id>/follow/', FollowViewSet.as_view({'post': 'follow'}), name='user-follow'),
    path('users/<int:user_id>/unfollow/', FollowViewSet.as_view({'post': 'unfollow'}), name='user-unfollow'),
    path('users/<int:user_id>/followers/', FollowersListView.as_view(), name='user-followers'),
    path('users/<int:user_id>/following/', FollowingListView.as_view(), name='user-following'),
]