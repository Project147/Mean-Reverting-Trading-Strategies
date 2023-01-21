import warnings
import OLS
warnings.simplefilter(action='ignore', category=FutureWarning)

from ImportData import ImportPriceData
from PairPotential import PairClusters
from PairValidator import PairValidate

# Set the start/end date for the price import class
start_date = "2021-12-25"
end_date = "2022-12-25"

# Import the prices with the given dates
import_price = ImportPriceData(start_date=start_date, end_date=end_date)
prices_sp500 = import_price.get_price_data(refresh_data=False)
returns_sp500 = import_price.get_returns_data()

# Form the clusters, i.e. the potential pairs.
selector: PairClusters = PairClusters(prices_sp500, returns_sp500)
selector.optics()
potential_pairs = selector.create_potential_pairs(display_pairs_info=True)
#selector.plot_tsne()

# Create the strategy validator
validator = PairValidate(price_data=prices_sp500, pairs_data=potential_pairs)
validatedPairs = validator.apply_filters()
validator.visualize_pairs(individualize=False, normalize=True)
validator.visualize_pairs(individualize=True) # For common plots of pairs
import OLS 
for pair in validatedPairs:
    #OLS.doPairPnl(pair[0],pair[1])
    OLS.doStrategy(pair[0],pair[1])