from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
from tgbot.binance import indicators as ind

from tgbot.misc.data import timeframe1, timeframe2, timeframe3

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI


def get_data(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    userid = str(userid)
    cur.execute('SELECT * FROM users ')
    users = cur.fetchall()
    for user in users:
        if user[0] == userid:
            timeframe = user[2]
            pair = user[3]
    base.commit()
    cur.close()
    base.close()
    return timeframe,pair

def get_param(userid):
    timeframe, pair = get_data(userid)
    if timeframe in timeframe1:
        sma = 24
        ema = 10
    elif timeframe in timeframe2:
        sma = 35
        ema = 15
    elif timeframe in timeframe3:
        sma = 60
        ema = 22
    return sma,ema

def get_ind(userid):
    timeframe, pair = get_data(userid)
    klines = botB.klines(
        symbol=pair,
        interval=TIMEFRAME,
        limit=KLINES_LIMITS
    )
    klines = klines[:len(klines)-int(not USE_OPEN_CANDLES)]
    closes = [float(x[4]) for x in klines]
    high = [float(x[2]) for x in klines]
    low = [float(x[3]) for x in klines]
    
    smaP,emaP = get_param(userid)
    sma = ind.SMA(closes, smaP)
    ema = ind.EMA(closes, emaP)
    macd ,macdsignal = ind.MACD(closes,10,15,30)
    rsi = ind.RSI(closes, 14)
    return sma,ema,rsi, macd ,macdsignal, closes
    
    
def calculate(userid):
    sma, ema, rsi, macd, macdsignal, bars = get_ind(userid) 
    answer = 0
    
    if ema[-1] > sma[-1]:
        answer += 10
    else:
        answer += 2

    if macd[-1] > macdsignal[-1]:
        answer += 5
    else:
        answer += 1
        
    if int(rsi[-1]) > 60:
        answer +=8
    elif int(rsi[-1]) < 30:
        answer +=1
        
    return answer
    
