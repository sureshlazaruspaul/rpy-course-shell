import json
import numpy as np
from icecream import ic # type: ignore
from pathlib import Path

# loops concepts
# for loops, range, len, indexing

# Looping with range


# Looping over a list
# a. string list
my_list1 = ['apple', 'banana', 'cherry']






# b. numeric list
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]






# Looping over a numpy array
arr = np.array([10, 20, 30, 40, 50])





# fetch json data from file
current_dir = Path.cwd()
full_path = current_dir.parent.parent.joinpath("data", "trades.json")

# to read a json file
with open(full_path, "r", encoding="utf-8") as input_file:
    json_data = json.load(input_file)

# ic(json_data)

# # Looping over json data
# print("printing keys from json data")

# print("printing values from json data")

# print("printing items from json data")

# print("printing keys, values, items from json data")

