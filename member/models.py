from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Bisa ditambah field lain seperti 'phone_number' atau 'bio'
    phone_number = models.CharField(max_length=20, blank=True, null=True)
