import os
import requests
import asyncio

from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API_KEY')
base_url = 'http://api.weatherapi.com/v1'

def get_weather(city, user_choice):
    if user_choice == "Погода сейчас":    
        try:
            response = requests.get(f'{base_url}/current.json?key={api}&q={city}&lang=ru')
        except requests.RequestException as e:
            return f"⚠️ Не удалось подключиться к сервису погоды: {e}"
        data = response.json()
        if "error" in data:
            return f"❌ Город не найден: {data['error']['message']}"
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
            response = requests.get(f'{base_url}/forecast.json?key={api}&q={city}&days=5&lang=ru')
        except requests.RequestException as e:
            return f"⚠️ Не удалось подключиться к сервису погоды: {e}"
        data = response.json()
        if "error" in data:
                    return f"❌ Город не найден: {data['error']['message']}"
        forecast = [f'Прогноз на 5 дней в городе {data['location']['name']}, {data['location']['country']}:\n']
        try:
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
            text = 'error'
            return f"⚠️ Ошибка при получении данных: {e}"
    

