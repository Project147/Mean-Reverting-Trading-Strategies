from utils import utils


ticker1 = "NOKUSD=X"
ticker2 = "EURUSD=X"

client = utils(ticker1,ticker2)
client.read_data()
