from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "habit",
        "sign_of_a_pleasant_habit",
        "related_habit",
        "reward",
    )
    list_filter = ("sign_of_a_pleasant_habit",)
    search_fields = ("habit",)