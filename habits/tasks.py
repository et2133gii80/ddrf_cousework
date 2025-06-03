from celery import shared_task
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_message_to_user():
    habits = Habit.objects.filter(sign_of_a_pleasant_habit=False)
    for habit in habits:
        habit.send_indicator -= 1
        if not habit.send_indicator:
            if habit.owner.tg_chat_id:
                message = f"У вас сегодня выполнение привычки: {habit.habit}, которую нужно выполнить в {habit.time_execution} в {habit.place_of_execution}"
                send_telegram_message(message=message, chat_id=habit.owner.tg_chat_id)
                habit.send_indicator = habit.periodicity
        habit.save(update_fields=["send_indicator"])