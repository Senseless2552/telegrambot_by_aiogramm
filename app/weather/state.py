from aiogram.fsm.state import State, StatesGroup

class Weather(StatesGroup):
    choosed_forecast = State()
    city = State()
