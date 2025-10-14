import os
import asyncio
import sys
import dotenv

from aiogram import Bot, Dispatcher
from app.database.models import create_db
from app.handlers import router
from app.weather.handlers import weather_router
from app.profile.handlers import form_router

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher()

async def main():
    await create_db()
    dp.include_routers(router, weather_router, form_router)
    print('Бот запущен')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')
        sys.exit(1)