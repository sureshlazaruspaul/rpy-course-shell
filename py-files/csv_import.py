#----------------------------------------------------------------------
# author: Suresh Paul
# date: November 2025
# objective: CSV import and export using pandas
#   This script showcases how to read a CSV file into a pandas DataFrame,
#   perform some basic data manipulation, and then export the DataFrame
#   back to a CSV file.
# optional prerequisites: pandas, icecream
# learning outcomes:
# - Understand how to read CSV files using pandas
# - Learn how to manipulate DataFrames
# - Gain experience in exporting DataFrames to CSV files
# - Familiarity with file path handling using pathlib
# - type annotations using typing module
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# import all libraries
#----------------------------------------------------------------------
from icecream import ic # type: ignore

# new libraries
# for path and file storage handling
from pathlib import Path

# for dataframe (csv) treatment
import pandas as pd

