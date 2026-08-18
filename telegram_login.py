from telethon import TelegramClient

api_id = 36508047
api_hash = "1f5480f7967289974236f9dc1b6adef5"

client = TelegramClient("phat_pheang_session", api_id, api_hash)

client.start()

print("✅ Telegram login successful")

client.disconnect()