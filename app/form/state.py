from aiogram.fsm.state import State, StatesGroup

class Profile(StatesGroup):
    option = State()
    new_profile = State()
    get_profile = State()