import numpy as np
import matplotlib.pyplot as plt

from tgbot.misc.calc_indicators import get_ind, get_data



async def build_chart(userid):
    fig = plt.figure()
    
    userid = str(userid)
    
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    
    sma, ema, rsi, macd, macdsignal, bars = get_ind(userid)
    timeframe, pair = get_data(userid)

    x = np.array(range(60))


    ax1.plot(x,sma[-60:],color='red',label='SMA')
    ax1.plot(x,ema[-60:],color='blue',label='EMA')
    ax2.plot(x,rsi[-60:],color='purple',label='RSI')
    ax2.plot(x,(x * 0) + 50,color='grey',linestyle='--',alpha=0.5)
    ax2.plot(x,(x * 0) + 25,color='grey',linestyle='--',alpha=0.5)
    ax3.plot(x,macd[-60:],color='green',label='MACD')
    ax3.plot(x,macdsignal[-60:],color='red',label='MACDsignal')
    ax4.plot(x,bars[-60:],color='blue',label=pair)
    
    ax2.set_xlim(0,60)
    ax2.set_ylim(15,60)
    ax1.set_xlim(0,60)
    ax3.set_xlim(0,60)
    ax4.set_xlim(0,60)
    
    ax1.legend(loc='lower left')
    ax2.legend(loc='lower left')
    ax3.legend(loc='lower left')
    ax4.legend(loc='lower left')
    
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    fig.savefig('tgbot/img/' + str(userid) + '.png')
    
    return True