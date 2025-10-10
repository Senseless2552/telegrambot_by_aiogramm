from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

weather = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Погода сейчас")], [KeyboardButton(text = "Прогноз погоды на 5 дней")],
    [KeyboardButton(text = "Выход")]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

exit = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Выход")]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')