from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mail.ru",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password("1234")
        user.save()
