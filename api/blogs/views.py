from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser
from blog.models import Post
from api.blogs.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["author", "title"]
    pagination_class = None


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser]
