from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router, F

from app.weather.get_weater import get_weather
import app.weather.keyboard as kb
from app.weather.state import Weather

weather_router = Router()

@weather_router.message(CommandStart())
async def command_weather_handler (message: Message, state: FSMContext):
    await state.set_state(Weather.choosed_forecast)
    await message.answer('Привет! Я погодный бот, разработанный Михеевым Романом!! Выбери пункт из меню:', reply_markup=kb.weather)

@weather_router.message(Weather.choosed_forecast, F.text.in_({"Погода сейчас", "Прогноз погоды на 5 дней"}))
async def city_handler (message: Message, state: FSMContext):
    await state.update_data(choosed_forecast=message.text)
    await state.set_state(Weather.city)
    await message.answer('Напиши погоду какого города ты хочешь посмотреть:', reply_markup=kb.exit)

@weather_router.message(Weather.choosed_forecast)
async def unknow_city_handler(message: Message, state: FSMContext):
    await message.answer('Выбери пожалуйста пункт из меню', reply_markup=kb.weather)

@weather_router.message(Weather.city)
async def weather_handler(message: Message, state: FSMContext):
    city = message.text
    data = await state.get_data()
    user_choice = data.get("choosed_forecast")
    result = get_weather(city, user_choice)
    if result.startswith(("❌", "⚠️", "error")):
        await message.answer(
            f"{result}\nПожалуйста, введите корректное название города:",
        )
    else:
        await message.answer(result)
        await state.clear()

    
@weather_router.message(F.text.in_({"Выход"}))
async def exit_handler(message: Message, state: FSMContext):
    await message.answer('Выход....', reply_markup=ReplyKeyboardRemove())
    await state.clear()
