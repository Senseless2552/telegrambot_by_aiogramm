from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Погода')],[KeyboardButton(text='Мой ГитХаб')],
    [KeyboardButton(text='Выход')],[KeyboardButton(text='Профиль')],
], resize_keyboard=True, one_time_keyboard=True , input_field_placeholder='Выберите пункт меню.')


options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мой ГитХаб', url='https://github.com/Senseless2552')]
])


