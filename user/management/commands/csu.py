import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from config.settings import ENV_DIR
from user.models import Users

load_dotenv(ENV_DIR)


class Command(BaseCommand):
    """Create superuser command"""
    def handle(self, *args, **options):
        user = Users.objects.create(
            email=os.getenv('ADMIN_EMAIL'),
            first_name='Admin',
            last_name='Artem',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('POSTGRES_PASSWORD'))
        user.save()
