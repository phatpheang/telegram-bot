import requests
import time
from datetime import datetime

BOT_TOKEN = "8701587966:AAFFlZu17xB88gJmQeez0YAoPo1DyVEWQ7w"
CHAT_ID = "-1004300120862"

last_message = ""

while True:

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    message = f"""
🔔 PHAT PHEANG 68 EXCHANGE

🥇 GOLD
BUY : 4365
SELL: 4375

💵 USD
BUY : 4041
SELL: 4061

🇹🇭 THB
BUY : 121.7
SELL: 122.2

⏰ {current_time}

Telegram: @lenghoor
"""

    if message != last_message:

        response = requests.post(
            "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": message
            }
        )

        print(response.text)

        last_message = message

    print("Checking...")

    time.sleep(60)