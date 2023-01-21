import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class utils:
    def __init__(self,ticker1,ticker2):
        self.ticker1 = ticker1
        self.ticker2 = ticker2
        self.ticker1_close = []
        self.ticker2_close= []
        self.read_data()
        

    def read_data(self):
        pair1 = yf.Ticker(self.ticker1)
        hist1 = pair1.history(period="3mo")
        for x in hist1["Close"]:
            self.ticker1_close.append(x)
        

        pair2 = yf.Ticker(self.ticker2)
        hist2 = pair2.history(period="3mo")
        for x in hist2["Close"]:
            self.ticker2_close.append(x)       
        
        self.check_date()

        #plt.plot(self.ticker1_close)
        #plt.plot(self.ticker2_close)
        #plt.show()

    def check_date(self):
        if (len(self.ticker1_close ) > len(self.ticker2_close)):
            self.ticker1_close = self.ticker1_close[-len(self.ticker2_close):]
        else:
            self.ticker2_close = self.ticker2_close[-len(self.ticker2_close):]

  





