import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value

#KAFKA CONFIG
KAFKA_BROKER = get_env_var("KAFKA_BROKER")
KAFKA_TOPIC = get_env_var("KAFKA_TOPIC")
STREAM_URL = get_env_var("STREAM_URL")

#PSQL CONFIG
DB_HOST = get_env_var("DB_HOST")
DB_PORT = get_env_var("DB_PORT")
DB_NAME = get_env_var("DB_NAME")
DB_USER = get_env_var("DB_USER")
DB_PASSWORD = get_env_var("DB_PASSWORD")

#DISCORD BOT CONFIG
DISCORD_BOT_TOKEN = get_env_var("DISCORD_BOT_TOKEN")