from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

form = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать новый профиль', callback_data='new_profile')], 
    [InlineKeyboardButton(text='Мой профиль', callback_data='get_profile')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')],
])

exit = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Выход")]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')