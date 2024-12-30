from bot import Bot

import time
import matplotlib.pyplot as plt
import numpy as np
from builtinfunc.data_wrangling import read_data







# init bot with starting money
fiat_start = 100
fiat = fiat_start
crypto = 0
bot = Bot(fiat)
history = read_data()
count = 0
buys = 0
sells = 0
Ispos= 0
Pnl = []
hurst_value=[]


t = np.arange(0, len(history), 1)

for current_value in history:
    count += 1
    #decision = bot.tick(current_value)
    decision = bot.tick_hurst(current_value)
    HUrst_param=bot.Get_Hurst_chan_value(current_value)
    hurst_value.append(HUrst_param)
  

    
    if decision == 'WAIT':
        pass
    elif decision == 'BUY':
        #if Ispos == 0:
                 
           # buys += 1
          #  crypto = 0.5*fiat / current_value
         #   fiat = 0.5*fiat
        #elif Ispos == 1:

        buys += 0
        crypto = fiat / current_value
        fiat = 0
    elif decision == 'SELL':
       
        #  clear exit here 
        #if Ispos == 1:
        sells += 1
        fiat = crypto * current_value
        crypto = 0.0

    bot.update_currency(crypto, fiat)

    print ('Tick', count, ':', current_value, ', crypto:', crypto, ' / fiat:', fiat, ', decision:', decision,"pnl",crypto * current_value + fiat, "HUrstValue", hurst_value[-1])
    Pnl.append(crypto * current_value + fiat)
    
    
    
    print ('Tick', count, ':', current_value, ', crypto:', crypto, ' / fiat:', fiat, ', decision:', decision)
    time.sleep(0.01)

# summary
if crypto > 0.1:
    fiat = crypto * current_value
    
profit = (fiat-fiat_start)/fiat_start * 100
    
print('From', fiat_start, 'to', fiat, ', profit:', round(profit, 2), '%, buys:', buys, ', sells:', sells)


fig, axs = plt.subplots(3, 1, layout='constrained')
axs[0].plot(t, Pnl)
# 






# 
# 
# axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Pnl and Crypto_value')
axs[0].grid(True)
axs[1].plot( t, history)
#axs[2].axline(y=0.5,color = 'r', linestyle = ':', label = "blue line") 
  
axs[2].plot( t, hurst_value, t,0.5*(t+1)/(t+1))






plt.show()

