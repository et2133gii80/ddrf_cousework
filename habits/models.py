
from datetime import timedelta

from django.core.validators import MaxValueValidator
from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    """
    Модель привычки
    """
    habit = models.CharField(
        max_length=255,
        verbose_name="Привычка",
    )
    place_of_execution = models.CharField(
        max_length=255, verbose_name="Место где нужно выполнять привычку",
        **NULLABLE
    )
    time_execution = models.TimeField(
        verbose_name="Время когда выполняется привычка",
        **NULLABLE
    )
    periodicity = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(7)],
        verbose_name="Периодичность привычки",
        default=1
    )
    time_to_complete = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="Продолжительность выполнения привычки по времени",
    )
    sign_of_a_pleasant_habit = models.BooleanField(
        verbose_name="Показатель приятной привычки",
        default=False
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная приятная привычка",
        **NULLABLE,
        related_name="related_habits"
    )
    reward = models.CharField(
        verbose_name="Вознаграждение за привычку",
        **NULLABLE
    )

    STATUS_PUBLISHED = [
        ("Опубликован", "Опубликован"),
        ("Не опубликован", "Не опубликован"),
    ]
    published = models.CharField(
        max_length=50,
        choices=STATUS_PUBLISHED,
        default="Не опубликован",
        verbose_name="Статус опубликования привычки",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        related_name="users_habits",
        **NULLABLE
    )
    send_indicator = models.PositiveSmallIntegerField(
        editable=False,
        verbose_name="Индикатор отправки",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("id",)

    def __str__(self):
        return self.habit

