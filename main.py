import asyncio
import threading

from discord_bot.bot import run_bot
from kafka_service import consume
from kafka_service import push_to_kafka


async def main():
    consumer_task = asyncio.create_task(consume())

    producer_thread = threading.Thread(target=push_to_kafka, daemon=True)
    producer_thread.start()

    discord_bot_thread = threading.Thread(target=run_bot)
    discord_bot_thread.start()

    await consumer_task

if __name__ == "__main__":
    asyncio.run(main())