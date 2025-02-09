import asyncio
import json
import logging
from aiokafka import AIOKafkaConsumer
from db.dto import RecentChangesDTO
from config import KAFKA_BROKER, KAFKA_TOPIC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = RecentChangesDTO()

async def consume():
    """
    Kafka Consumer that reads messages and saves them to the database
    """
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id="recent_changes_group",
        auto_offset_reset="earliest"
    )

    await consumer.start()
    try:
        async for msg in consumer:
            try:
                data = json.loads(msg.value.decode("utf-8"))
                await db.save_recent_change(data)

            except Exception as e:
                logger.error(f"Unexpected error: {e}")

    finally:
        await consumer.stop()
        logger.info("Kafka Consumer stopped.")

