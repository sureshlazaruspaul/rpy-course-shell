#----------------------------------------------------------------------
# author: Suresh Paul
# date: November 2025
# objective: Date handling basics in pandas
#   This script showcases how to read a CSV file containing date
#   information, convert various date formats to pandas datetime format,
#   extract date components, perform date arithmetic, select and drop
#   columns, and extract columns as arrays or lists. Finally, it 
#   demonstrates how to manipulate the DataFrame and export it back 
#   to a CSV file.
# optional prerequisites: pandas, icecream, pathlib, typing
# learning outcomes:
# - Understand how to read CSV files using pandas
# - Learn to convert various date formats to pandas datetime format
# - Gain skills in extracting date components (year, month, day, day of week)
# - Perform date arithmetic (adding/subtracting days, calculating differences)
# - Learn to select and drop columns in a DataFrame
# - Extract columns as numpy arrays or Python lists
# - Familiarity with file path handling using pathlib
# - type annotations using typing module
#----------------------------------------------------------------------

# import all libraries
import pandas as pd
from icecream import ic # type: ignore
from pathlib import Path

# fetch the directory where data is situated
current_dir = Path.cwd()
parent_dir = current_dir.parent.parent
dir_path = parent_dir.joinpath("data")

# fetch a file
filename = "dates.csv"
file_fullpath = dir_path.joinpath(filename)
ic(file_fullpath)

# import data
dates_df = pd.read_csv(file_fullpath)
ic(dates_df)

# describe the dataframe
ic(dates_df.head())  # display top 5 rows of the dataframe
ic(dates_df.tail())  # display bottom 5 rows of the dataframe
ic(dates_df.shape)   # display basic information about the dataframe
ic(dates_df.columns) # display columns information
ic(dates_df.dtypes)  # display data types information
ic(dates_df.index)   # display index information

# Define various date formats present in the dataset
date_formats = [
    "%Y-%m-%d",        # 2023-01-15
    "%m-%d-%Y",        # 01-15-2023
    "%d-%m-%Y",        # 15-01-2023
    "%d/%m/%Y",        # 15/01/2023
    "%d/%m/%y",        # 15/01/23
    "%Y.%m.%d",        # 2023.01.15
    "%B %d, %Y",       # January 15, 2023
    "%d %B %Y",        # 15 January 2023
    "%d %b %Y",        # 15 Jan 2023
]

#-----------------------------------------------------------------------------------------------------
# CREATE A NEW VARIABLE FOR FORMATTED DATES
# Syntax: dataframe.loc[:, "new_date_column"]
#-----------------------------------------------------------------------------------------------------
# Converting various date formats to pandas datetime format
# syntax: pd.to_datetime(date_as_string, format="date_format")
#-----------------------------------------------------------------------------------------------------
# Convert DATE1 column to datetime format
# Convert DATE2 column to datetime format
# Convert DATE3 column to datetime format


#-----------------------------------------------------------------------------------------------------
# Extracting date components
# syntax: dataframe["date_column"].dt.component
#-----------------------------------------------------------------------------------------------------
# e.g., year, month, day, day_name() [day of week]
# Add extracted components as new columns


#-----------------------------------------------------------------------------------------------------
# Date arithmetic: Calculate difference between two dates
#-----------------------------------------------------------------------------------------------------
# Calculate difference between a given date in string format and a date variable in date format
given_date_str = "20230101"



# Calculate days since given date and create a new column days_since_given_date
# or use .dt.days to get integer days

# Add/Delete 3 days to formatted_DATE1 and create a new column Three_Days_Later using pd.Timedelta(days=N)


#-----------------------------------------------------------------------------------------------------
# Selecting and Dropping columns
#-----------------------------------------------------------------------------------------------------
keep_some_vars_df = dates_df.copy()
delete_some_vars_df = dates_df.copy()

# Define a list of variables to keep
keep_list = ["year", "month", "day"]

# Define a list of variables to drop
drop_list = ["DATE1", "DATE2", "DATE3"]

# Safely keep only the selected columns
# Safely drop the selected columns 


#-----------------------------------------------------------------------------------------------------
# Extracting a column as a np.ndarray using .to_numpy() or a list using .tolist()
#-----------------------------------------------------------------------------------------------------

