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
