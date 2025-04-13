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

## 🚀 Running the App

1. Clone the Repository
```
git clone https://github.com/shoghik11/nats-subscriber-app.git
cd nats-subscriber-app
```

2. Create .env file
```
DB_HOST=postgres
DB_PORT=5432
DB_NAME=messages_db
DB_USER=user
DB_PASSWORD=password

NATS_URL=nats://nats:4222
NATS_SUBJECT=messages
```
3. Start Services via Docker Compose

```
docker-compose up --build
```

4. Publishing Messages to NATS

In a new terminal, use the official NATS CLI:
```
nats pub messages "Hello from NATS!"
```

5. Checking Stored Messages
To manually inspect stored messages:
```
docker exec -it nats_subscriber_app-postgres-1 psql -U user -d messages_db
```
Then run:
```
SELECT * FROM messages;
```


## 📁 Project Structure
```
nats_subscriber_app/
├── app/
│   ├── api/
│   │   └── subscriber.py
│   ├── data/
│   │   ├── database.py
│   │   └── repository.py
│   └── service/
│       └── processor.py
├── .env
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```
