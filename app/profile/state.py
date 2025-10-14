from aiogram.fsm.state import State, StatesGroup

class Profile(StatesGroup):
    option = State()
    new_profile = State()
    name = State()
    age = State()
    hobby = State()
    sex = State()
    photo = State()
    get_profile = State()