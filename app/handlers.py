import os
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from dotenv import load_dotenv
import requests
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler (message: Message):
    await message.answer('Привет! Я погодный бот, разработанный Михеевым Романом!! Выбери пункт из меню:', reply_markup=kb.main)

@router.message(F.text == "Погода сейчас")
async def menu_handler (message: Message):
    await message.answer('Выбери город из меню:', reply_markup=kb.city)

@router.message(F.text == "Обо мне")
async def about_handler (message: Message):
    await message.answer('Мой гитхаб:', reply_markup=kb.options)

@router.message(F.text)
async def weather_handler(message: Message):
    match message.text:
        case 'Москва':
            weather = get_weather('Moscow')
            await message.answer(f'Сейчас в {message.text} {weather} градусов цельсия',reply_markup=kb.main)
        case 'Курск':
            weather = get_weather('Kursk')
            await message.answer(f'Сейчас в {message.text} {weather} градусов цельсия',reply_markup=kb.main)
        case 'Санкт-Петербург':
            weather = get_weather('Saint Petersburg')
            await message.answer(f'Сейчас в {message.text} {weather} градусов цельсия',reply_markup=kb.main)
        case 'Екатеринбург':
            weather = get_weather('Ekaterinburg')
            await message.answer(f'Сейчас в {message.text} {weather} градусов цельсия',reply_markup=kb.main)


load_dotenv()
api = os.getenv('API_KEY')
base_url = 'http://api.weatherapi.com/v1'

def get_weather(city):
    response = requests.get(f'{base_url}/current.json?key={api}&q={city}&lang=ru')
    data = response.json()
    temp = data['current']['temp_c']
    return temp
