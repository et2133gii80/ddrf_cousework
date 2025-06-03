
from rest_framework import serializers
from habits.models import Habit
from habits.validators import (FieldFillingValidator, RelatedHabitValidator,
                               execution_time_validator)


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.DurationField(
        validators=[execution_time_validator],
        required=False
    )

    class Meta:
        model = Habit
        exclude = ("send_indicator",)
        validators = [
            FieldFillingValidator(
                "reward",
                "related_habit",
                "sign_of_a_pleasant_habit"
            ),
            RelatedHabitValidator("related_habit"),
        ]
