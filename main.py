import os
import asyncio
import sys
import dotenv

from aiogram import Bot, Dispatcher, html
from app.handlers import router

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)

dp = Dispatcher()

async def Main():
    dp.include_router(router)
    print('Бот запущен')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(Main())
    except KeyboardInterrupt:
        print('Бот остановлен')
        sys.exit(1)