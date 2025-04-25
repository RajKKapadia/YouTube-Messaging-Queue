import time
import os

from celery import Celery
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

celery_app = Celery(main="telegram_tasks", broker="pyamqp://guest:guest@localhost//")

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


@celery_app.task
def process_message_and_respond(chat_id: str, text: str):
    time.sleep(10)
    response = f"AI response to: {text}"
    send_telegram_message(chat_id, response)
    return "Message processed"


def send_telegram_message(chat_id: str, text: str):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    return response.json()
