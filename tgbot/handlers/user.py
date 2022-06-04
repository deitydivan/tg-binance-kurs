from aiogram import Router
from aiogram.types import Message
from tgbot.binance.config import (bot, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
from tgbot.binance import indicators as ind

user_router = Router()

def tests():
    klines = bot.klines(
        symbol='BTCUSDT',
        interval=TIMEFRAME,
        limit=KLINES_LIMITS
    )
    klines = klines[:len(klines)-int(not USE_OPEN_CANDLES)]
    closes = [float(x[4]) for x in klines]
    high = [float(x[2]) for x in klines]
    low = [float(x[3]) for x in klines]
    # Скользящая средняя
    sma_5 = ind.SMA(closes, 5)
    sma_100 = ind.SMA(closes, 100)
    ema_5 = ind.EMA(closes, 5)
    ema_100 = ind.EMA(closes, 100)
    macd = ind.MACD(closes,10,15,30)
    return macd


@user_router.message(commands=["start"])
async def user_start(message: Message):
    await message.reply('time')
