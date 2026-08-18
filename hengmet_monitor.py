from telethon import TelegramClient

api_id = 36508047
api_hash = "1f5480f7967289974236f9dc1b6adef5"

client = TelegramClient(
    "phat_pheang_session",
    api_id,
    api_hash
)

async def main():

    channel = await client.get_entity("hengmet")

    messages = await client.get_messages(channel, limit=50)

    for msg in messages:

        if msg.photo:

            print("Found photo:", msg.id)

            file_path = await msg.download_media(
                file=r"C:\ExchangeBot\images"
            )

            print("Downloaded:", file_path)

            break

with client:
    client.loop.run_until_complete(main())