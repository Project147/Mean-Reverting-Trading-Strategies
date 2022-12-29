import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as stat
import statsmodels.tsa.stattools as ts

###############################################################
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


class Strategy:
    """
    """

    def __init__(self, price_data: pd.DataFrame, pairs_data):
        self.__price_data = price_data
        self.__pairs_data = np.array(pairs_data)

    def compute_spred(self):
        return self