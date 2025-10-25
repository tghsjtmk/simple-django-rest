## 🕐 Sesi 3 - Membuat App Blog (30 menit)

### 📦 Buat App `blog`

```bash
python manage.py startapp blog
```

`blog/models.py`:

```python
from django.db import models
from member.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Tambahkan ke `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    # apps
    "member",
    "blog",
]
```

`blog/admin.py`:

```python
from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
```

Migrasi:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 🔗 Coba di Browser

- Running Django → [http://localhost:8000](http://localhost:8000)
- Running Admin → [http://localhost:800/admin](http://localhost:8000)

---
