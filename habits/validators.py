
from datetime import timedelta
from rest_framework.validators import ValidationError


class FieldFillingValidator:
    def __init__(self, reward, related_habit, sign_of_a_pleasant_habit):
        self.reward = reward
        self.related_habit = related_habit
        self.sign_of_a_pleasant_habit = sign_of_a_pleasant_habit

    def __call__(self, value):
        reward_field = value.get(self.reward)
        related_habit_field = value.get(self.related_habit)
        sign_of_a_pleasant_habit_field = value.get(self.sign_of_a_pleasant_habit)

        if reward_field and related_habit_field:
            raise ValidationError(
                "Может быть заполнено поле reward или поле related_habit"
            )
        if sign_of_a_pleasant_habit_field:
            if reward_field or related_habit_field:
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения"
                )
        else:
            if not reward_field and not related_habit_field:
                raise ValidationError(
                    "Поле reward или поле related_habit обязательно для заполнения у полезной привычки"
                )


class RelatedHabitValidator:
    def __init__(self, related_habit):
        self.related_habit = related_habit

    def __call__(self, value):
        habit = value.get(self.related_habit)
        if habit:
            if not habit.sign_of_a_pleasant_habit:
                raise ValidationError("Связанная привычка должна быть приятной")


def execution_time_validator(value):
    if value:
        if value > timedelta(seconds=120):
            raise ValidationError(
                "Продолжительность выполнения привычки не может быть более 120 секунд"
            )
