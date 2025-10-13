from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Router, F
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start_handler (message: Message):
    await message.answer('Привет, что бы ты хотел сделать?', reply_markup=kb.main)
@router.message(F.text.in_({'Мой ГитХаб'}))
async def about_handler (message: Message):
    await message.answer('Вот ссылка:', reply_markup=kb.options)
