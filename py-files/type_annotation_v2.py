# type: ignore
# file: type_annotation.py
#------------------------------------------------------------------------------------------------------------
# purpose: Demonstrate type annotations in Python
# author: Suresh Paul
# date: 2025-11-10
#------------------------------------------------------------------------------------------------------------
# what is type annotation?
#------------------------------------------------------------------------------------------------------------
# Type annotation is a feature in Python that allows 
# the coder to specify the expected data types of variables,
# function parameters, and return values. 
# This helps improve code readability, maintainability, 
# and can assist with static type checking.
#------------------------------------------------------------------------------------------------------------

from pathlib import Path
import numpy as np 
import pandas as pd
import logging
from typing import List, Dict, Any

# log package setup

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)
# Example usage: success: ✅, warning: ⚠️, error: ❌ ❗


#------------------------------------------------------------------------------------------------------------
# popular type annotations in Python
#------------------------------------------------------------------------------------------------------------

# integer type annotation

age: int = 24

# float type annotation

speed: float = 9.8

logger.info(f"✅ Variable 1: {age}, Type: {type(age)}")
logger.info(f"✅ Variable 2: {speed}, Type: {type(speed)}")

# string type annotation

file_location: str = "C:\data\iris.csv"
logger.info(f"✅ Variable 3: {file_location=}, Type: {type(file_location)=}")

# boolean type annotation

isTrue: bool = True
logger.info(f"✅ Variable 4: {isTrue=}, Type: {type(isTrue)=}")


# Path type annotation

filepath: Path = Path(file_location)
logger.info(f"✅ Variable 5: {filepath=}, Type: {type(filepath)=}")

iris_df: pd.DataFrame = pd.read_csv(filepath)
logger.info(f"✅ {iris_df=}")
logger.info(f"✅ {type(iris_df)=}")

# pandas type annotation

# I. list type annotation
# - list can contain numerics or strings

# a. list type annotation of numerics (int)

list_of_integers: list = [1, 2, 3, 6, 78, 9000, 2657]
logger.info(f"✅ Object 6: {list_of_integers=}, Type: {type(list_of_integers)=}")

list_of_integers_v2: List[int] = [1, 2, 3, 6, 78, 9000, 2657] 
logger.info(f"✅ Object 6A: {list_of_integers=}, Type: {type(list_of_integers)=}")

# b. list type annotation of numerics (float)

list_of_decimals: list = [1.0, 20.5, 3.602, 25.45, 78.26, 8.889]
logger.info(f"✅ Object 7: {list_of_decimals=}, Type: {type(list_of_decimals)=}")

list_of_decimals_v2: List[float] = [1.0, 20.5, 3.602, 25.45, 78.26, 8.889]
logger.info(f"✅ Object 7A: {list_of_decimals_v2=}, Type: {type(list_of_decimals_v2)=}")


# c. list type annotation of strings

random_list_of_strings: list = ["GIS", "DELL", "CSX", "TSLA", "MU", "NVDA", "This is a text"]
logger.info(f"✅ Object 8: {random_list_of_strings=}, Type: {type(random_list_of_strings)=}")

random_list_of_strings_v2: List[str] = ["GIS", "DELL", "CSX", "TSLA", "MU", "NVDA", "This is a text"]
logger.info(f"✅ Object 8A: {random_list_of_strings_v2=}, Type: {type(random_list_of_strings_v2)=}")




# II. numpy array type annotation
# - numpy array can contain numerics or strings

# a. numpy type annotation

sales: List[int] = [250, 350, 450, 550, 650, 750]

sales_as_numpy: np.ndarray = np.array(sales)
logger.info(f"✅ Object 9: {sales_as_numpy=}, Type: {type(sales_as_numpy)=}")


# III. dictionary type annotation
# key: value pairs
# key is a string
# value can be of any type: integer or a float - so, Any

grades: dict = {
    "Aidan": "A",
    "Brian": "B+", 
    "Mekensey": "A",
    "Paul": "D"
}
logger.info(f"✅ Object 10: {grades=}, Type: {type(grades)=}")


grades_v2: Dict[str, Any] = {
    "Aidan": "A",
    "Brian": "B+", 
    "Mekensey": "A",
    "Paul": "D"
}
logger.info(f"✅ Object 10A: {grades_v2=}, Type: {type(grades_v2)=}")