# import all libraries
import numpy as np # type: ignore
from icecream import ic

# Things to remember:
# 1. Numpy arrays allow for efficient mathematical operations on 
#    entire arrays without the need for explicit loops.
# 2. Element-wise operations can be performed using standard operators (+, -, *, /) or 
#    numpy functions (np.add, np.subtract, np.multiply, np.divide).
# 3. Icecream library provides a convenient way to print variables.

# Syntax to remember:
# np.array, np.add, np.subtract, np.multiply, np.divide, np.zeros_like, np.concatenate

# Objective: 
# Calculate GROSS PROFIT, GROSS MARGIN, DEBT-EQUITY RATIO, and BALANCE SHEET EQUATION 
# from financial data using numpy arrays.


# input a vector (list) of financial data from yahoo finance
# AAPL Income Statement (in thousands)
sales = [416160000, 391035000, 383285000, 394328000, 365817000]
cogs = [220960000, 210352000, 214137000, 223546000, 212981000]

# AAPL Balance Sheet (in thousands)
total_assets = [359240000, 364980000, 352583000, 352755000, 351002000]
total_liabilities = [285510000, 308030000, 290437000, 302083000, 287912000]
total_equity = [73730000, 56950000, 62146000, 50672000, 63090000]








# fetching data for EBIT and EBITDA
ebit = [133050000, 123216000, 114301000, 119437000, 111852000]
ebitda =[144750000, 134661000, 125820000, 130541000, 123136000]