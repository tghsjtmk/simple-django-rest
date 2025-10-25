## 🧩 Sesi 2 Setup User Model di App `member` (30 menit)

### 📁 Struktur Folder Awal

```
playground/
  settings.py
member/
  models.py
  admin.py
  apps.py
manage.py
.env
requirements.txt
```

---

### 🔐 1. Membuat Model `User`

`member/models.py`

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Bisa ditambah field lain seperti 'phone_number' atau 'bio'
    pass
```

---

### ⚙️ 2. Registrasi di `settings.py`

Tambahkan di `INSTALLED_APPS` dan set `AUTH_USER_MODEL`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "member",
]

AUTH_USER_MODEL = "member.User"
```

---

### 🧑‍💻 3. Buat Superuser Otomatis (Opsional)

Buat file `member/management/commands/generate_superuser.py`:

```python
import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from member.models import User

class Command(BaseCommand):
    help = "Generate Superuser automatically if not exists"

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")
        if not User.objects.filter(username=username).exists():
            call_command("createsuperuser", "--noinput")
```

### ⚙️ 4. Konfigurasi Environment & Database

Buat `.env`:

```bash
touch .env
```

Tambahkan env variable di `.env`:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123
```

`playground/settings.py`:

```python
import environ, os

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

DATABASES = {"default": env.db()}
```

---

### ⚙️ 5. Migrasi & Jalankan

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py generate_superuser
python manage.py runserver
```

### 🔗 Coba di Browser

- Running Django → [http://localhost:8000](http://localhost:8000)
- Running Admin → [http://localhost:800/admin](http://localhost:8000)

---
