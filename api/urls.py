from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("blogs/", include("api.blogs.urls")),
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
