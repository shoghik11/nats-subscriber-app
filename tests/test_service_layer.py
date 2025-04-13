
import pytest
import asyncio
from app.service.processor import process_message

@pytest.mark.asyncio
async def test_process_message_valid():
    await process_message("Hello World")

@pytest.mark.asyncio
async def test_process_message_empty():
    await process_message("")
