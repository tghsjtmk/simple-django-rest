## 🧱 Sesi 5 — CRUD Blog API (30 menit)

### 📁 Struktur API

```
api/
  blogs/
    serializers.py
    views.py
    urls.py
  urls.py
```

---

### `serializers.py`

```python
from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author_name", "published_at"]
```

---

### `views.py`

```python
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser
from blog.models import Post
from api.blogs.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-published_at")
    parser_classes = [MultiPartParser]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "content"]
    filterset_fields = ["author"]
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
```

---

### `urls.py` (di `api/blogs`)

```python
from django.urls import path
from api.blogs.views import PostListCreateAPIView, PostDetailAPIView

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
]
```

---

### `api/urls.py`

```python
from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("blogs/", include("api.blogs.urls")),
]
```

---

## 🚀 Jalankan Server

```bash
python manage.py runserver
```

### 🔗 Coba di Browser

- List Post → [http://localhost:8000/api/blogs/posts/](http://localhost:8000/api/blogs/posts/)
- Swagger Docs → [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Auth Login → [http://localhost:8000/api/auth/login/](http://localhost:8000/api/auth/login/)

---
