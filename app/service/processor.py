
from app.data.repository import save_message

async def process_message(message: str):
    if not message.strip():
        print("Ignoring empty message")
        return
    print(f"Processing message: {message}")
    await save_message(message)
