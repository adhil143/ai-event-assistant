# 🔐 Load environment variables
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# 📩 Function to send message
def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    params = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.get(url, params=params)

    print("Status:", response.status_code)
    print("Response:", response.text)