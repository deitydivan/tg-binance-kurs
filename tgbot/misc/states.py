from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

class getPre(StatesGroup):
    pair = State()
    timeframe = State()
    
    