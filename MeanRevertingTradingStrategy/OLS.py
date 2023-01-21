from utils import utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.api import OLS
from statsmodels import api as sm

###################### SOME CONSTANT ##########################
###############################################################


spread = 'SPREAD'
moving_average = "MOVING AVERAGE"
moving_average_std_dev = "MOVING AVERAGE STD"
up_band = "UPPER BAND"
low_band = "LOWER BAND"
long_entry = "long entry"
short_entry = "short entry"
long_exit = "long exit"
short_exit = "short exit"
LONG_POSITION = "LONG POSITION"
SHORT_POSITION = "SHORT POSITION"
POSITIONS = "POSITIONS"
SPREAD_DIFFERENCE = "SPREAD DIFFERENCE"
PNL = "PNL"
CUM_PNL = "CUMULATIVE PNL"
TIME = 1000
##############################################################
##############################################################

def doStrategy(ticker1, ticker2):

    x,y = doPairPnl(ticker1, ticker2)
    list_pnl = mean_reverting_strategy(x,y)
    if list_pnl[-1] > 0:
        plt.plot(list_pnl)
        plt.title(ticker1 + " " + ticker2)
        plt.show()
def doPairPnl(ticker1, ticker2):

    client = utils(ticker1,ticker2)
    df = pd.concat([pd.DataFrame(client.ticker1_close),pd.DataFrame(client.ticker2_close)], axis = 1)
    df.columns = [ticker1, ticker2]
    return list(df[ticker1]), list(df[ticker2])

def mean_reverting_strategy(stock1_prices, stock2_prices):
    # Create a spread by subtracting the prices of one stock from the other
    spread = np.array(stock1_prices) - np.array(stock2_prices)

    # Fit an OLS model to the spread
    ols_model = sm.OLS(spread, np.ones(len(spread))).fit()

    # Get the mean and standard deviation of the residuals (errors) from the OLS fit
    spread_mean = ols_model.resid.mean()
    spread_std = ols_model.resid.std()

    # Initialize variables to keep track of the position and cumulative PnL
    position = None
    cumulative_pnl = 0
    list_cumulative_pnl = []

    for i in range(1, len(spread)):
        if position is not None:
            if position == "long":
                pnl = (stock1_prices[i] - long_price) - (stock2_prices[i] - short_price)
            else:
                pnl = (short_price - stock1_prices[i]) - (long_price - stock2_prices[i])
            cumulative_pnl += pnl
            list_cumulative_pnl.append(cumulative_pnl)
            position = None

        # Check if the spread is currently more than 2 standard deviations away from the mean
        if spread[i] - spread_mean > 2 * spread_std:
            # If it is, enter a short position in stock1 and a long position in stock2
            if position != "short":
                position = "short"
                short_price = stock1_prices[i]
                long_price = stock2_prices[i]
        elif spread[i] - spread_mean < -2 * spread_std:
            # If it is, enter a long position in stock1 and a short position in stock2
            if position != "long":
                position = "long"
                long_price = stock1_prices[i]
                short_price = stock2_prices[i]



    return list_cumulative_pnl

