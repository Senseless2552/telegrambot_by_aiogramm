from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router, F
import app.form.keyboards as kb
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.form.state import Profile

form_router = Router()

@form_router.message(F.text == 'Профиль')
async def form_handler (message: Message, state: FSMContext):
    await state.set_state(Profile.option)
    await message.answer('Выберите опцию:', reply_markup=kb.form)

@form_router.callback_query(Profile.option, F.data == 'new_profile')
async def new_form_handler (message: Message, state: FSMContext):
    await state.update_data(options=CallbackQuery.data)
    await state.set_state(Profile.new_profile)
    await message.answer('Введите имя:', reply_markup=kb.exit)
    if message.text == 'Выход':
        await message.answer('Выход....', reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return
    user_name = message.text
    await message.answer('Введите ваш возраст:', reply_markup=kb.exit)
    user_age = message.text
    await message.answer('Какие у вас хобби?', reply_markup=kb.exit)
    user_hobby = message.text
    await message.answer('Какого вы пола?', reply_markup=kb.exit)
    user_sex = message.text

@form_router.callback_query(F.data == 'my_form')
async def my_form_handler (message: Message):
    ...

@form_router.callback_query(F.data == 'exit')
async def exit_handler (message: Message):
    ...