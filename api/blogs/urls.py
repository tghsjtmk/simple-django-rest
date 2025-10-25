from django.urls import path
from api.blogs.views import PostListCreateAPIView, PostDetailAPIView

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
]
