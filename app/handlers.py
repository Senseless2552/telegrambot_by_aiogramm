from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, F
import app.keyboards as kb

router = Router()

@router.message(F.text == "Обо мне")
async def about_handler (message: Message):
    await message.answer('Мой гитхаб:', reply_markup=kb.options)
