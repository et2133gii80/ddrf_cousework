import requests
from config.settings import TELEGRAM_BOT_ID


def send_telegram_message(message, chat_id):
    params = {"text": message, "chat_id": chat_id}
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_ID}/sendMessage", params=params)
