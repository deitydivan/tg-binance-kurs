from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from tgbot.config import load_config
from datetime import datetime

from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
from tgbot.binance import indicators as ind

from tgbot.misc.texts import messages
from tgbot.misc.af_status import af_status
from tgbot.misc.get_info import get_profile
from tgbot.misc.get_time import get_time

from tgbot.db.users_update import reg_user, add_set
user_router = Router()

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


@user_router.message(commands=["start"])
async def user_start(message: Message):
    userid = message.from_user.id
    name = message.from_user.first_name
    
    status = await af_status(userid)
    if status == False:
        await reg_user(userid,name)
    await bot.send_message(userid, messages["gretting"])
    
@user_router.message(commands=["help"])
async def user_start(message: Message):
    userid = message.from_user.id
    
    await bot.send_message(userid, messages["help"])
    
@user_router.message(commands=["instructions"])
async def user_start(message: Message):
    userid = message.from_user.id
    
    await bot.send_message(userid, messages["instructions"])
    
@user_router.message(commands=["profile"])
async def user_start(message: Message):
    userid = message.from_user.id
    name, advices = await get_profile(userid)
    time = get_time()
    print(type(time))
    
    await bot.send_message(userid,f"Ваш id: {userid}\nИмя: {name}\nКоличество полученых сигналов: {advices}" )
    
@user_router.message(commands=["getcur"])
async def user_start(message: Message):
    userid = message.from_user.id
    
    file = FSInputFile('tgbot/misc/crypto.txt')
    await bot.send_document(userid, file)
