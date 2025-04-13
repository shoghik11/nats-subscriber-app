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
