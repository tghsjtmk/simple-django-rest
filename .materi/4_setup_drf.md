## 🕐 Sesi 4 - Setup Django REST Framework (50 menit)

### 📦 Install Package Tambahan

```bash
pip install djangorestframework django-cors-headers django-filter
pip install dj-rest-auth 'django-allauth[socialaccount]' djangorestframework-simplejwt
pip install drf-spectacular drf-spectacular-sidecar
```

Tambahkan ke `settings.py`:

```python
INSTALLED_APPS = [
    ...
    # libs
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
    "allauth.account.middleware.AccountMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True
```

Tambahkan versi ke `requirements.txt`:

```txt
djangorestframework==3.16.1
django-cors-headers==4.9.0
django-filter==25.2

dj-rest-auth==7.0.1
django-allauth==65.12.1
django-allauth[socialaccount]==65.12.1
djangorestframework-simplejwt==5.5.1

drf-spectacular==0.28.0
drf-spectacular-sidecar==2025.10.1
```

Konfigurasi DRF & JWT:

```python
from datetime import timedelta

# drf_spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "Simple Blog API",
    "DESCRIPTION": "Dokumentasi API Blog Sederhana",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": True,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

# DRF
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
}

# allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_FIELDS = ["username*", "email*", "password1*", "password2*"]
ACCOUNT_LOGIN_METHODS = ["username", "email"]
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_GET = False

# dj-rest-auth
REST_USE_JWT = True
REST_AUTH = {
    "USE_JWT": True,
    "TOKEN_MODEL": None,
    "JWT_AUTH_HTTPONLY": False,
    "JWT_AUTH_RETURN_EXPIRATION": True,
}

# simplejwt
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

---

Buat Folder `api` untuk handle Rest Api:

### `api/urls.py`

```python
from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
]

# Enable swagger doc
if settings.DEBUG:
    urlpatterns += [
        # YOUR PATTERNS
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        # Optional UI:
        path(
            "docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
```

---

Tambahkan urls api kedalam project directory:

### `playground/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
```

Migrasi:

```bash
python manage.py migrate
python manage.py runserver
```

---
