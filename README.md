This project listens to the live Wikimedia data stream, which tracks real-time changes on Wikipedia. It uses Kafka to process data efficiently, stores it in a database with a Kafka consumer, filters the data, and displays results through Discord bot commands.

The system runs asynchronously, launching:
- Kafka Producer (fetches live stream data)
- Kafka Consumer (processes and stores data)
- Discord Bot (handles user commands to display filtered data)
