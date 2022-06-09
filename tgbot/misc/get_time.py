from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
from datetime import datetime

def get_time():
    time = botB.time()
    time = time['serverTime']
    # print(datetime.fromtimestamp(time['serverTime']))
    
    return time 