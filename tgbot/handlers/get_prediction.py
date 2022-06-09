from aiogram import Router, Bot, types
from aiogram.types import Message
from aiogram.dispatcher.filters.content_types import ContentTypesFilter
from tgbot.config import load_config

from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
from tgbot.binance import indicators as ind

from tgbot.misc.texts import messages
from tgbot.misc.data import timeframe as tf
from tgbot.misc.get_all_crypto import get_all_crypto
from tgbot.misc.calc_indicators import calculate

from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from tgbot.misc.states import getPre

from tgbot.db.users_update import reg_user, add_set,update_counter
import json

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

get_router = Router()



@get_router.message(commands=["get"])
async def user_start(message: Message, state = FSMContext):
    userid = message.from_user.id
    
    await bot.send_message(userid, messages["send_currecy"])
    await state.set_state(getPre.pair)
    
@get_router.message(content_types=types.ContentType.TEXT, state = getPre.pair)
async def user_start(message: Message, state = FSMContext):
    userid = message.from_user.id
    crypto = await get_all_crypto()
    user_pair = message.text.upper()
    if user_pair in crypto:
        
        await state.update_data(pair = user_pair)
        
        await bot.send_message(userid, messages["send_timeframe"])
        await state.set_state(getPre.timeframe)
    else:
        await bot.send_message(userid, "Нет такой пары, введите еще раз")
        await state.set_state(getPre.pair)
    
    
@get_router.message(content_types=types.ContentType.TEXT, state = getPre.timeframe)
async def user_start(message: Message, state = FSMContext):
    userid = message.from_user.id
    
    await state.update_data(timeframe=message.text)
    
    if message.text not in tf:
        await bot.send_message(userid, "Неверный timeframe\n" + messages["send_timeframe"])
        await state.set_state(getPre.timeframe)
    else:
        await bot.send_message(userid, "Проверяем наши индикаторы...")
        await state.update_data(timeframe=message.text)
        user_data = await state.get_data()
        await add_set(user_data['timeframe'],user_data['pair'],userid)    
        await state.clear()
        
        prediction = calculate(userid)
        if prediction >= 18:
            await bot.send_message(userid, messages["short"])
        elif prediction <= 4:
            await bot.send_message(userid, messages["long"])
        else:
            await bot.send_message(userid, messages["netrual"])
        
        await update_counter(userid)
        await bot.send_message(userid, messages["warning"])
        
        
    