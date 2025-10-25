from django.urls import path
from api.blogs.views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    PostCommentsAPIView,
    PostCommentsDetailAPIView,
)

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("comments/", PostCommentsAPIView.as_view(), name="post-detail"),
    path("comments/<int:pk>/", PostCommentsDetailAPIView.as_view(), name="post-detail"),
]
