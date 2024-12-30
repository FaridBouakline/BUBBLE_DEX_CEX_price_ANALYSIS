'''
source : https://www.linkedin.com/pulse/rolling-hurst-exponent-python-trading-jakub-polec-e92yf/
'''

#!/usr/bin/python
from __future__ import division
import time
import numpy as np 
import math
from scipy import stats
from builtinfunc.generic_func import apply_rolling_function ,hurst_chan
class Bot:
    """ Class for a Trading bot """
    crypto = 0
    fiat = 0
    buy_limit = 0.5     # buy at 4050% of average
    sell_limit = 1-buy_limit    # sell at 50% of average
    buy_price = 0.0
    memory_limit = 180  # maximum memory
    memory_lower = 60   # minimum amount of data to make first BUY / SELL decision
    memory = []
    BUY = 'BUY'
    SELL = 'SELL'
    WAIT = 'WAIT'

    def __init__(self, fiat):
        self.memory = []
        self.fiat = fiat
        self.buy_price = 0.0
        self.signal = 0.0
       

    def tick(self, current_value):
        ''' decision algorithm what to do on update '''
        # save to memory
        if len(self.memory) >= self.memory_limit:
            self.memory.pop(0)
        self.memory.append(current_value)
        
        if len(self.memory) < self.memory_lower:
            # if not enough data, do nothing
            return self.WAIT
        
        lower = self.get_percentile(self.buy_limit)
        upper = self.get_percentile(self.sell_limit)
        
        print (' > lower:', lower, ', upper:', upper)
        
        if self.crypto <= 0.0:
            # no crypto: could BUY or WAIT
            if current_value < upper:
                self.buy_price = current_value
                return self.BUY
        elif self.fiat <= 0.0:
            # no fiat: could SELL or WAIT
            if current_value > upper and current_value > self.buy_price:
                return self.SELL
       
                
        # no decision made, wait and drink tea
        return self.WAIT



    def tick_hurst(self,current_value):
        ''' 
        decision algorithmsimple hurst implementation
         if h> 0.5--> buy (implement sell with futures version)
         if h < 0.5 --> men revertinf technique
         if h=0.5 no pattern wait and see (ensure nom position)
           '''
        # save to memory
        if len(self.memory) >= self.memory_limit:
            self.memory.pop(0)
        self.memory.append(current_value)
        
        if len(self.memory) < self.memory_lower:
            # if not enough data, do nothing
            return self.WAIT
        




        lower = self.get_percentile(self.buy_limit)
        upper = self.get_percentile(self.sell_limit)
        
        print (' > lower:', lower, ', upper:', upper)
        HUrst_chan_value=self.hurst_chan_bot(l=len(self.memory)//3) 
     
       
        
        if self.crypto <= 0.1:
            # no crypto: could BUY or WAIT
            if HUrst_chan_value >= 0.5 and  current_value> upper:
                self.buy_price = current_value
                return self.BUY
            else:
                return self.WAIT
        elif self.fiat <= 0.1:

            # no fiat: could SELL or WAIT
            if HUrst_chan_value >0.5 and current_value >= upper:
                return self.WAIT
            if HUrst_chan_value > 0.5 and current_value <= lower:
                return self.SELL
            if HUrst_chan_value < 0.5:
                return self.SELL
           
        # no decision made, wait and drink tea
        return self.WAIT
    
    def Get_Hurst_chan_value(self,current_value):
 
           
        # save to memory
        if len(self.memory) >= self.memory_limit:
            self.memory.pop(0)
        self.memory.append(current_value)
        
        if len(self.memory) < self.memory_lower:
            # if not enough data, do nothing
            return 0
        




   
        return self.hurst_chan_bot(l=len(self.memory)//3) 

        


    def update_currency(self, crypto, fiat):
        self.crypto = crypto
        self.fiat = fiat
    
    def get_percentile(self, perc):
        sorted_memory = sorted(self.memory)
        item = int(perc * len(sorted_memory))
        return sorted_memory[item]
    
    def hurst_rs(self,lag1=2,lag2= None):
        """
        Calculates the Hurst Exponent using the Rescaled Range (R/S) analysis method.
        """
    # Compute log returns
          
        # Create an array of lag values
        if lag2 is None: 
         lag2 =len(self.memory) // 3
        
        lags = range(2, lag2)
        # Compute log returns
        log_returns = np.diff(np.log(self.memory))
        
        # Calculate the array of the variances of the lagged differences
        tau = [np.sqrt(np.std(np.subtract(log_returns[lag:], log_returns[:-lag]))) for lag in lags]
        
        # Use a linear fit to estimate the Hurst Exponent
        print("lags)")
        print(lags)
        poly = np.polyfit(np.log(lags), np.log(tau), 1)
        
        # The Hurst exponent is the slope of the linear fit
        hurst_exponent = poly[0]*2.0
        
        # The fractal dimension is related to the Hurst exponent
        fractal_dimension = 2 - hurst_exponent
        
        return hurst_exponent, fractal_dimension 
    
    def hurst_chan_bot(self, l):
        return hurst_chan(self.memory, l=l)