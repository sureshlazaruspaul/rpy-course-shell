import numpy as np
from icecream import ic # type: ignore

# input a vector (list) of financial data from yahoo finance
# AAPL Income Statement (in thousands)
sales = [391035000, 383285000, 394328000, 365817000]
sales = np.array(sales)

cogs = [210352000, 214137000, 223546000, 212981000]
cogs = np.array(cogs)

# AAPL Balance Sheet (in thousands)
total_assets = [364980000, 352583000, 352755000, 351002000]
total_assets = np.array(total_assets)

total_liabilities = [308030000, 290437000, 302083000, 287912000]
total_liabilities = np.array(total_liabilities)

total_equity = [56950000, 62146000, 50672000, 63090000]
total_equity = np.array(total_equity)
#----------------------------------------------------------------------

