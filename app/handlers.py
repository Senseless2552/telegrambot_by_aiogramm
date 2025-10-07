from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler (message: Message):
    await message.answer('Привет!', reply_markup=kb.options)


    