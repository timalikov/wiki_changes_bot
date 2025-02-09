import json
import logging
import requests
import sseclient
from kafka import KafkaProducer

from config import KAFKA_BROKER, STREAM_URL, KAFKA_TOPIC
from serializers import serialize_event_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
                    
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    retries=5
)

def push_to_kafka():
    client = sseclient.SSEClient(STREAM_URL)  

    for event in client:
        try:
            data = json.loads(event.data)
            parsed_data = serialize_event_data(data)
            
            producer.send(KAFKA_TOPIC, value=parsed_data) 
        except Exception as e:
            logger.error("Error processing event: %s", str(e))
            