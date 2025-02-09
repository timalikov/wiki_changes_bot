This project listens to the live Wikimedia data stream, which tracks real-time changes on Wikipedia. It uses Kafka to process data efficiently, stores it in a database with a Kafka consumer, filters the data, and displays results through Discord bot commands.

The system runs asynchronously, launching:
- Kafka Producer (fetches live stream data)
- Kafka Consumer (processes and stores data)
- Discord Bot (handles user commands to display filtered data)

## Setup Instructions

1. **Python Setup**  
   - Create a virtual environment:  
     ```sh
     python -m venv venv  
     source venv/bin/activate  # On Windows: venv\Scripts\activate  
     ```  
   - Install dependencies:  
     ```sh
     pip install -r requirements.txt  
     ```  
   - ⚠ **Note**: Use **Python < 3.13** to avoid dependency issues.  

2. **Kafka Setup**  
   - Install Kafka and start the server.  
   - Create a topic for streaming data.  

3. **Database Setup**  
   - Install PostgreSQL and create a database.  
   - Tables will be created automatically when running the code.  

4. **Environment Variables**  
   - Check `.env.example` and fill in your local configuration in `.env`.
  
5. Run the Project
     ```sh
     python main.py
     ```

## Code structure
- **`main.py`** – Entry point of the project. It runs:  
  - **Kafka Consumer** asynchronously (`consume()`).  
  - **Kafka Producer** in a separate thread (`push_to_kafka`).  
  - **Discord Bot** in another thread (`run_bot`).  

- ### **Database (`db/` folder)**  
  - **`base.py`** – Manages database connections using **connection pooling** for efficiency.  
  - Uses **`asyncpg`** for async PostgreSQL interaction.  
  - **Creates tables** automatically on startup for easy setup.  
  - Provides an **async context manager** for connections.
- ### **Database DTOs (`db/dto/` folder)**  
  - Stores **DTO (Data Transfer Object) classes** for structured interaction with the database.  
  - Each DTO **inherits** from `BasePsqlDTO` to manage database connections efficiently.  
  - Provides **methods for querying, inserting, and updating** data in the DB.  
- ### **Discord Bot (`discord_bot/` folder)**  
  - **Contains all bot-related code.**  
  - **`bot.py`** – Sets up and launches the bot, managing commands.  
  - Loads bot commands (`SetLangCommand`, `RecentChangesCommand`, `StatsCommand`) as **Cogs**.  
  - **Why Cogs?**  
    - **Modular structure** – Each command is in its own file for better organization.  
    - **Easier maintenance** – Commands can be updated without modifying `bot.py`.  
    - **Scalability** – New features can be added as separate Cogs without cluttering the main bot file.
   
- ### **Discord Bot Commands (`discord_bot/commands/` folder)**  
  - Contains **modular command Cogs**, each handling a specific bot function.  
  - Commands use **slash commands (`@app_commands.command`)**.  
  - Supports **autocomplete choices**, which are stored separately in `command_choices.py` for cleaner code and easier updates.  
  - Commands interact with the database via **DTO classes** to process and store user data.
 
- ### **Kafka (`kafka_service/` folder)**  
  - Handles **real-time data streaming** using Kafka.
  - #### **Kafka Producer (`push_to_kafka()`)**  
    - Listens to the **Wikimedia live stream**.  
    - Parses, **serializes event data** and sends it to **Kafka topic**.  
    - Uses **retries** for fault tolerance.
  - #### **Kafka Consumer (`consume()`)**  
    - Reads messages from **Kafka** asynchronously using `AIOKafkaConsumer`.  
    - Parses data and **stores it in the database**.  



