import os
import requests
import asyncio
import aiohttp

from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API_KEY')
base_url = 'http://api.weatherapi.com/v1'


async def get_weather_async(city, user_choice):
    if user_choice == "Погода сейчас":    
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{base_url}/current.json?key={api}&q={city}&lang=ru') as response:
                    data = await response.json()
        except aiohttp.ClientError as e:
            return f"⚠️ Не удалось подключиться к сервису погоды: {e}"
        try:
            text = (
                f'Сейчас в городе {data['location']['name']}, {data['location']['country']}:\n'
                f'🌡Температура: {data['current']['temp_c']}°C.\n'
                f'💨Скорость ветра: {data['current']['wind_kph']} км\ч.\n'
                f'☁️Погодные условия: {data['current']['condition']['text']}.\n'
            )
            return text
        except KeyError as e:
            text = 'error'
            return f"⚠️ Ошибка при получении данных: {e}"
    elif user_choice == "Прогноз погоды на 5 дней":
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{base_url}/forecast.json?key={api}&q={city}&days=5&lang=ru') as response:
                    data = await response.json()
        except aiohttp.ClientError as e:
            return f"⚠️ Не удалось подключиться к сервису погоды: {e}"
        try:
            forecast = [f'Прогноз на 5 дней в городе {data['location']['name']}, {data['location']['country']}:\n']
            for day in data['forecast']['forecastday']:
                text = (
                    f'День {day['date']}. \n'
                    f'🌡️ Средняя температура: {day['day']['avgtemp_c']}°C. \n'
                    f'💨 Макс. скорость ветра: {day['day']['maxwind_kph']} км\ч. \n'
                    f'☁️ Погодные условия: {day['day']['condition']['text']}. \n'
                )
                forecast.append(text)
            return "\n".join(forecast)
        except KeyError as e:
            return f"⚠️ Ошибка при получении данных: {e}"


