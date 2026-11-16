# file: functions_basics.py
# numerical operation functions
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗

import numpy as np
import logging
from typing import List, Union
from icecream import ic

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# input a vector (list) of financial data from yahoo finance
# AAPL Income Statement (in thousands)
sales: List[int] = [391035000, 383285000, 394328000, 365817000]
sales_as_ndarray: np.ndarray = np.array(sales)

cogs: List[int] = [210352000, 214137000, 223546000, 212981000]
cogs_as_ndarray: np.ndarray = np.array(cogs)

# AAPL Balance Sheet (in thousands)
total_assets: List[int] = [364980000, 352583000, 352755000, 351002000]
total_assets_as_ndarray: np.ndarray = np.array(total_assets)

total_liabilities: List[int] = [308030000, 290437000, 302083000, 287912000]
total_liabilities_as_ndarray: np.ndarray = np.array(total_liabilities)

total_equity: List[int] = [56950000, 62146000, 50672000, 63090000]
total_equity_as_ndarray: np.ndarray = np.array(total_equity)
#----------------------------------------------------------------------

# def func_name(args):
#     pass

# add two numbers


# subtract two numbers


# multiply two numbers


# divide two numbers


# find the average of a list of numbers


# find the maximum of a list of numbers


# join two lists


# check if number is there in a numpy array or list


# add two numpy arrays


# subtract two numpy arrays


# multiply two numpy arrays


# divide two numpy arrays



# array operations



# array operations with early return

