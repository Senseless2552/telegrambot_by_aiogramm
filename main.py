import os
import asyncio

from aiogram import Bot, Dispatcher, html
from dotenv import load_dotenv
from app.handlers import router

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)

dp = Dispatcher()

async def Main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(Main())