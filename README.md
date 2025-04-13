# NATS Subscriber App

A simple Python-based 3-layered application that listens to messages on a [NATS](https://nats.io/) subject, processes them, and stores them in a PostgreSQL database.

---

## 🧠 Architecture Overview

This app follows a **3-layered architecture**:

1. **API Layer**  
   - Connects to NATS and listens for messages on a subject.
   - File: `app/api/subscriber.py`

2. **Service Layer**  
   - Handles message validation and business logic.
   - File: `app/service/processor.py`

3. **Data Layer**  
   - Manages PostgreSQL interactions using `asyncpg`.
   - Files:  
     - `app/data/database.py`: Database connection pool  
     - `app/data/repository.py`: Message persistence

---

## ⚙️ Technologies Used

- Python 3.10+
- NATS Messaging System
- PostgreSQL 15
- Docker & Docker Compose
- `asyncpg`, `python-dotenv`, `nats-py`

---

## 📝 PostgreSQL Schema

SQL to create the `messages` table:

```sql
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    received_at TIMESTAMPTZ DEFAULT NOW()
);
```

## 🚀 Running the Application

Clone the Repository
```
git clone https://github.com/shoghik11/nats-subscriber-app.git
cd nats-subscriber-app
```

### Via Docker Compose (Recommended)

To start the services, run the following command from the root directory of your project:
```
docker-compose up
```

This will spin up:
- The NATS server
- A PostgreSQL container
- Your Python subscriber application

### Via Python (Without Docker)

1. Install the required dependencies:
```
pip install -r requirements.txt
```

2. Create a .env file in the root directory and configure the environment variables as follows:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=messages_db
DB_USER=user
DB_PASSWORD=password
NATS_URL=nats://localhost:4222
NATS_SUBJECT=messages
```

3. Run the application:
```
python -m app.api.subscriber
```
This will connect to the NATS server, subscribe to the messages subject, and start listening for messages.

## 📊 Verifying Data in PostgreSQL
To check the stored messages:
1. Access the PostgreSQL container:
```
docker exec -it nats_subscriber_app-postgres-1 psql -U user -d messages_db
```
2. Run:
```
SELECT * FROM messages;
```

You should see a list of stored messages with timestamps.

## 💼 Project Structure

```text
nats_subscriber_app/
├── app/
│   ├── api/
│   │   └── subscriber.py
│   ├── service/
│   │   └── processor.py
│   └── data/
│       ├── database.py
│       └── repository.py
├── docker-compose.yml
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 📦 Credits
Made for educational purposes for CS322: Software Engineering course.
