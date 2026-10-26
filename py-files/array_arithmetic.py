# file: array_arithmetic.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌, 
#                add: ➕, subtract: ➖, multiply: ✖️, divide: ➗

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def array_arithmetic(arr1, arr2, operation):
   
    op = operation.lower()

    # operations
    if op == "add":
        return np.add(arr1, arr2)

    elif op == "subtract":
        return np.subtract(arr1, arr2)

    elif op == "multiply":
        return np.multiply(arr1, arr2)

    elif op == "divide":
        return np.divide(arr1, arr2, out=np.full_like(arr1, np.nan, dtype=float), where=(arr2 != 0))

    return np.array([], dtype=float)
