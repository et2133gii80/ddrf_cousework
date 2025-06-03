from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        **NULLABLE
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        **NULLABLE
    )
    tg_chat_id = models.PositiveIntegerField(
        verbose_name="ID чата в Telegram",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.email