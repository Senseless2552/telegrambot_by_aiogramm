from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Погода сейчас")],
    [KeyboardButton(text = "Обо мне")]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мой ГитХаб', url='https://github.com/Senseless2552')]
])

city = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Москва')], [KeyboardButton(text='Курск')],
    [KeyboardButton(text='Санкт-Петербург')], [KeyboardButton(text='Екатеринбург')]
])