from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
import json

async def get_all_crypto():
    cryptos = botB.exchangeInfo()
    answer = []
    text = cryptos['symbols']
    with open('tgbot/misc/crypto.txt', 'w') as fw:
        for i in text:
            fw.write(i['symbol'] + '\n')
            answer.append(i['symbol'] )
    return answer