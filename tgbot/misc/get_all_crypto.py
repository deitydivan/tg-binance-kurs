from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)

async def get_all_crypto():
    cryptos = botB.exchangeInfo()
    answer = []
    text = cryptos['symbols']
    for i in text:
        answer.append(i['symbol'])
    return answer