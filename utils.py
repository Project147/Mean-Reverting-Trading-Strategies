import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class utils:
    def __init__(self,ticker1,ticker2):
        self.ticker1 = ticker1
        self.ticker2 = ticker2
        self.ticker1_opens = []
        self.ticker2_opens= []
        

    def read_data(self):
        pair1 = yf.Ticker(self.ticker1)
        hist1 = pair1.history(period="max")
        for x in hist1["Open"]:
            self.ticker1_opens.append(x)
        

        pair2 = yf.Ticker(self.ticker2)
        hist2 = pair2.history(period="max")
        for x in hist2["Open"]:
            self.ticker2_opens.append(x)       
        
        self.check_date()

        plt.plot(self.ticker1_opens)
        plt.plot(self.ticker2_opens)
        plt.show()

    def check_date(self):
        if (len(self.ticker1_opens ) > len(self.ticker2_opens)):
            self.ticker1_opens = self.ticker1_opens[-len(self.ticker2_opens):]
        else:
            self.ticker2_opens = self.ticker2_opens[-len(self.ticker2_opens):]

  





