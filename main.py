import asyncio
import threading

from kafka_consumer import consume
from kafka_producer import push_to_kafka


async def main():
    consumer_task = asyncio.create_task(consume())

    producer_thread = threading.Thread(target=push_to_kafka, daemon=True)
    producer_thread.start()

    await consumer_task

if __name__ == "__main__":
    asyncio.run(main())