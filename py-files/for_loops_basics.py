# file: for_loops_basics.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️

import numpy as np
from typing import List
from icecream import ic

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

#-SAMPLE DATA---------------------------------------------------------------------------------------------------

# 1. 25 random non-sequential integers
integers = [
    42, 819, 7, 305, 991, 64, 512, 18, 734, 290,
    88, 643, 151, 902, 33, 476, 821, 109, 555, 24,
    778, 389, 610, 95, 417
]

# 2. 25 random non-sequential floats (4+ decimals)
floats = [
    14.8291, 0.0472, 93.5184, 7.6039, 52.1948,
    31.7405, 8.9261, 67.3812, 4.1597, 85.4026,
    19.6374, 73.2859, 2.8416, 46.9103, 61.0758,
    28.5941, 90.1237, 11.4682, 55.7924, 3.3185,
    79.8562, 37.0914, 64.2379, 16.5048, 82.9713
]

# 3. 25 first names
first_names = [
    "Liam", "Maya", "Noah", "Elena", "Caleb",
    "Sophia", "Lucas", "Aria", "Mason", "Chloe",
    "Ethan", "Zoe", "Logan", "Nora", "Julian",
    "Hannah", "Owen", "Lily", "Gavin", "Grace",
    "Isaac", "Hazel", "Leo", "Stella", "Miles"
]

# 4. 25 grocery items
grocery_items = [
    "Milk", "Eggs", "Sourdough Bread", "Bananas", "Chicken Breast",
    "Olive Oil", "Cheddar Cheese", "Spinach", "Jasmine Rice", "Tomatoes",
    "Greek Yogurt", "Garlic", "Almond Butter", "Coffee Beans", "Avocados",
    "Black Beans", "Oats", "Bell Peppers", "Salmon Fillets", "Butter",
    "Onions", "Pasta", "Honey", "Strawberries", "Soy Sauce"
]

#---------------------------------------------------------------------------------------------------------------

# simple loop over a default range



# simple loop over a string



# simple loop over a prescribed range with steps



# simple loop over a prescribed range in reverse steps



# loop over a predefined list of integers



# loop over a predefined list of strings



# loops over an numpy array



# sum of items in a list / numpy array



# appending to a new list



# looping over two lists simultaneously using zip


