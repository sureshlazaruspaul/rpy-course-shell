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

# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗

# def func_name(args):
#     pass

# add two numbers

def add_function(a, b):
    sum_two_var = a + b
    return sum_two_var

num1: float = 9.87
num2: float = 3.256

sum_num1_num2: float = add_function(num1, num2)
ic(sum_num1_num2)

# 
def add_function1(a: float, b: float) -> float:
    return a + b

ic(
    add_function1(num1, num2)
)

# subtract two numbers
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗

def sp_subtract(num1: float, num2: float) -> float:
    logger.info("➖ performing subtraction")
    return num1 - num2

ic(
    sp_subtract(5.2876, 3.4587)
)

# multiply two numbers
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗

def sp_multiply(value1: float, value2: float) -> float:
    logger.info("✖️ performing a multiplication")
    return value1 * value2

ic(
    sp_multiply(2, 6)
)

# divide two numbers
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗

def sp_divide(number1: float, number2: float) -> float:
    logger.info("➗ performing a division")
    if number2 == 0:
        logger.info("division by ZERO, Are you serious?")
        return 0
    return number1/number2

ic(
    sp_divide(22, 0)
)

# find the average of a list of numbers
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗

number_list: List[float] = [1.0, 5.2, 6.1, 6.3, 9.6, 5.555]

def sp_list_average(numlist: List[float]) -> float:
    # step 1: create a numpy array of the input list
    numlist_as_ndarray: np.ndarray = np.array(numlist)
    logger.info("list operation: compute mean of a list")
    # step 2: return mean()
    return numlist_as_ndarray.mean()

ic(
    sp_list_average(number_list)
)



def sp_list_average1(m: List[float]) -> float:
    counter1: int = 0
    sum_of_all_elements: float = 0.0

    for item in number_list:
        counter1 += 1
        sum_of_all_elements += item

    return sum_of_all_elements/counter1

ic(
    sp_list_average(number_list),
    sp_list_average1(number_list)
)
 


# find the maximum of a list of numbers
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗

def sp_listmax(p: List[float]) -> float:
    # step 1: convert list to numpy array
    p_as_ndarray = np.array(p)
    # step 2: return the max
    logger.info("find the max in a list")
    return p_as_ndarray.max()

ic(
    sp_listmax(number_list)
)



def sp_listmax_check(p: List[float], threshold: int) -> bool:
    # step 1: convert list to numpy array
    p_as_ndarray = np.array(p)
    # step 2: return the max
    logger.info("check the max in a list against threshold")

    if p_as_ndarray.max() > threshold:
        return True
    
    return False
    

ic(
    sp_listmax_check(number_list, 10)
)


def sp_listmax_check_v2(p: List[float], threshold: int) -> tuple[bool, float]:
    # step 1: convert list to numpy array
    p_as_ndarray = np.array(p)
    # step 2: return the max
    logger.info("check the max in a list against threshold")
    if p_as_ndarray.max() > threshold:
        return True, p_as_ndarray.max()   
    return False, p_as_ndarray.max()
    

isTrue, max_value = sp_listmax_check_v2(number_list, 10)

ic(isTrue, max_value)


# join two lists
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗



# check if number is there in a numpy array or list
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗



# add two numpy arrays
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗



# subtract two numpy arrays
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗



# multiply two numpy arrays
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗



# divide two numpy arrays
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗




# array operations
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗




# array operations with early return
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️
#                addition: ➕, subtraction: ➖, multiplication: ✖️, division: ➗


