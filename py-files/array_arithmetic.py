# type: ignore
# file: array_arithmetic.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌, 
#                add: ➕, subtract: ➖, multiply: ✖️, divide: ➗

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
