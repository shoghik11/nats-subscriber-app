
import asyncio
from nats.aio.client import Client as NATS
from app.service.processor import process_message
import os
from dotenv import load_dotenv

load_dotenv()

NATS_URL = os.getenv("NATS_URL")
SUBJECT = os.getenv("NATS_SUBJECT")

async def main():
    nc = NATS()
    await nc.connect(servers=[NATS_URL])

    async def message_handler(msg):
        data = msg.data.decode()
        await process_message(data)

    await nc.subscribe(SUBJECT, cb=message_handler)
    print(f"Subscribed to {SUBJECT}...")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
