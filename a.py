from utils import utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.api import OLS


###################### SOME CONSTANT ##########################
###############################################################

ticker1 = "NOKUSD=X"
ticker2 = "EURUSD=X"
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

##############################################################
##############################################################

client = utils(ticker1,ticker2)
df = pd.concat([pd.DataFrame(client.ticker1_close),pd.DataFrame(client.ticker2_close)], axis = 1)
df.columns = [ticker1, ticker2]

# calculate spread

model = OLS(df[ticker1].iloc[:len(df[ticker1])],df[ticker2].iloc[:len(df[ticker1])])
model.fit()
df[spread]  = df[ticker1] - model.normalized_cov_params[0] * df[ticker2]
df[spread].plot()
plt.ylabel("SPREAD")
plt.show()
df[moving_average] = df[spread].rolling(30).mean()
df[moving_average_std_dev] = df[spread].rolling(30).std()


#UPPER BAND AND LOWER BAND


df[up_band] = df[moving_average] + 2*df[moving_average_std_dev]
df[low_band] = df[moving_average] - 2*df[moving_average_std_dev]


#LONG POS

df[long_entry] = df[spread] < df[low_band]
df[long_exit] = df[spread] >= df[moving_average]


df[LONG_POSITION] = np.nan
df.loc[df[long_entry],LONG_POSITION] = 1
df.loc[df[long_exit],LONG_POSITION] = 0

df[LONG_POSITION] = df[LONG_POSITION].fillna(method='ffill')

#SHORT POSITION

df[short_entry] = df[spread] > df[up_band]
df[short_exit] = df[spread] <= df[moving_average]

df[SHORT_POSITION] = np.nan
df.loc[df[long_entry],SHORT_POSITION] = -1
df.loc[df[long_exit],SHORT_POSITION] = 0

df[SHORT_POSITION] = df[SHORT_POSITION].fillna(method='ffill')


df[POSITIONS] = df[LONG_POSITION] + df[SHORT_POSITION]

#PNL

df[SPREAD_DIFFERENCE]= df[spread] - df[spread].shift(1)
df[PNL] = df[POSITIONS].shift(1) + df[SPREAD_DIFFERENCE]
df[CUM_PNL] = df[SPREAD_DIFFERENCE].cumsum()

df[CUM_PNL].plot()
plt.xlabel("Date")
plt.ylabel(CUM_PNL)
plt.legend()
plt.show()