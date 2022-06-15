import math

# Simple moving average
def SMA(data, period):
    if len(data) == 0:
        raise Exception("Empty data")
    if period <= 0:
        raise Exception("Invalid period")

    interm = 0
    result = []
    nan_inp = 0
    
    for i, v in enumerate(data):
        if math.isnan(data[i]):
            result.append(math.nan)
            interm = 0
            nan_inp += 1
        else:
            interm += v
            if (i+1 - nan_inp) < period:
                result.append(math.nan)
            else:
                result.append(interm/float(period))
                if not math.isnan(data[i+1-period]):
                    interm -= data[i+1-period]
    return result

def SMMA(data, period):
    return generalEMA(data, period, 1/(float(period)))

# Calculates various EMA with different smoothing multipliers, see lower
def generalEMA(data, period, multiplier):
    if period <= 1:
        raise Exception("Invalid period")

    sma = SMA(data, period)
    
    result = []
    for k, v in enumerate(sma):
        if math.isnan(v):
            result.append(math.nan)
        else:
            prev = result[k-1]
            if math.isnan(prev):
                result.append(v)
                continue
            ema = (data[k]-prev)*multiplier + prev
            result.append(ema)
    return result

# Exponential moving average
def EMA(data, period):
    return generalEMA(data, period, 2/(float(period)+1.0))


# Moving average convergence/divergence
def MACD(data, fastperiod, slowperiod, signalperiod):
    macd, macdsignal, macdhist = [], [], []

    fast_ema = EMA(data, fastperiod)
    slow_ema = EMA(data, slowperiod)
    
    diff = []

    for k, fast in enumerate(fast_ema):
        if math.isnan(fast) or math.isnan(slow_ema[k]):
            macd.append(math.nan)
            macdsignal.append(math.nan)
        else:
            macd.append(fast-slow_ema[k])
            diff.append(macd[k])

    diff_ema = EMA(diff, signalperiod)
    macdsignal = macdsignal + diff_ema

    for k, ms in enumerate(macdsignal):
        if math.isnan(ms) or math.isnan(macd[k]):
            macdhist.append(math.nan)
        else:
            macdhist.append(macd[k] - macdsignal[k])

    # return macd, macdsignal, macdhist
    return macd ,macdsignal

# Relative strength index
def RSI(data, period):
    u_days = []
    d_days = []

    for i, _ in enumerate(data):
        if i == 0:
            u_days.append(0)
            d_days.append(0)
        else:
            if data[i] > data[i-1] :
                u_days.append(data[i] - data[i-1])
                d_days.append(0)
            elif data[i] < data[i-1]:
                d_days.append(data[i-1] - data[i])
                u_days.append(0)
            else:
                u_days.append(0)
                d_days.append(0)

    smma_u = SMMA(u_days, period)
    smma_d = SMMA(d_days, period)

    result = []

    for k, _ in enumerate(data):
        if smma_d[k] == 0:
            result.append(100)
        else:
            result.append(100 - (100 / (1 + smma_u[k]/smma_d[k])))

    return result