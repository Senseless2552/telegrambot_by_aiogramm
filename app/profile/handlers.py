from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram import Router, F
from app.database.requests import get_profile_by_id, set_profile_by_id
import app.profile.keyboards as kb
import app.keyboards as kbm
from aiogram.fsm.context import FSMContext
from app.profile.state import Profile

form_router = Router()

@form_router.message(F.text == 'Профиль')
async def form_handler (message: Message, state: FSMContext):
    await state.set_state(Profile.option)
    await message.answer('Выберите опцию:', reply_markup=kb.form)

@form_router.callback_query(Profile.option, F.data == 'new_profile')
async def new_form_handler (callback: CallbackQuery, state: FSMContext):
    await state.set_state(Profile.name)
    await callback.answer('Перевожу на создание профиля..')
    await callback.message.answer('Введите имя:', reply_markup=kb.exit)
    if callback.message.text == 'Выход':
        await callback.message.answer('Выход....', reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return
    
@form_router.message(Profile.name)
async def set_name (message: Message, state: FSMContext):
    if message.text == 'Выход':
        await message.answer('Выход....', reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return
    else:
        await state.update_data(name=message.text)
        await state.set_state(Profile.age)
        await message.answer('Введите возраст:', reply_markup=kb.exit)
    
@form_router.message(Profile.age)
async def set_age (message: Message, state: FSMContext):
    if message.text == 'Выход':
        await message.answer('Выход....', reply_markup=kbm.main)
        await state.clear()
        return
    else:
        try:
            user_age = int(message.text)
            if user_age > 150:
                await message.answer('Возраст должен быть не более 150!')
            elif user_age <= 0:
                await message.answer('Пожалуйста введите положительное число!')
            else:
                await state.update_data(age=user_age)
                await state.set_state(Profile.hobby)
                await message.answer('Введите ваши хобби:', reply_markup=kb.exit)
        except ValueError:
            await message.answer('Пожалуйста используйте цифры!')

@form_router.message(Profile.hobby)
async def set_hobby (message: Message, state: FSMContext):
    if message.text == 'Выход':
        await message.answer('Выход....', reply_markup=kbm.main)
        await state.clear()
        return
    else:
        await state.update_data(hobby=message.text)
        await state.set_state(Profile.sex)
        await message.answer('Выберите пол:', reply_markup=kb.sex)


@form_router.message(Profile.sex)
async def set_sex (message: Message, state: FSMContext):
    if message.text == 'Мужской':
        await state.update_data(sex=message.text)
        await state.set_state(Profile.photo)
        await message.answer('Пришлите вашу фотографию', reply_markup=kb.exit)
    elif message.text == 'Женский':
        await state.update_data(sex=message.text)
        await state.set_state(Profile.photo)
        await message.answer('Пришлите вашу фотографию', reply_markup=kb.exit)
    else:
        await message.answer('Можалйста выберите пункт из меню:', reply_markup=kb.sex)

@form_router.message(Profile.photo)
async def set_photo (message: Message, state: FSMContext):
    try:
        photo=message.photo[-1].file_id
        if message.text == 'Выход':
            await message.answer('Выход....', reply_markup=kbm.main)
            await state.clear()
            return
        else:
            await state.update_data(photo=photo)
            data = await state.get_data()
            try:
                await set_profile_by_id(tg_id = message.from_user.id, data = data)
                await message.answer('Ваш профиль успешно создан!', reply_markup=kbm.main)
                await state.clear()
            except Exception as e:
                await message.answer(f'Ошибка в созданни профиля, попробуй еще раз:', reply_markup=kbm.main)
                await state.clear()
    except TypeError:
        await message.answer('Пожалуйста отправьте фотографию!!')
@form_router.callback_query(Profile.option, F.data == 'get_profile')
async def get_profile(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Загружаю ваш профиль')
    tg_id = callback.from_user.id
    profile = await get_profile_by_id(tg_id=tg_id)
    
    if not profile:
        await callback.message.answer('У вас нет профиля, создайте его', reply_markup=kbm.main)
        return
    
    try:
        await callback.message.answer(f'Ваш профиль:')
        await callback.message.answer_photo(
            photo=profile.photo,
            caption=f'Имя: {profile.name}\nВозраст: {profile.age}\nХобби: {profile.hobby}\nПол: {profile.sex}'
        )
    except Exception as e:
        await callback.message.answer(f'Ошибка при загрузке профиля{e}', reply_markup=kbm.main)
    
    await state.clear()