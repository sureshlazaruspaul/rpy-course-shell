# type: ignore
#----------------------------------------------------------------------
# import all libraries
#----------------------------------------------------------------------
import numpy as np 
import pandas as pd
from icecream import ic
from pathlib import Path

#-----------------------------------------------------------------------------------------------------
# fetch the directory where data is situated
#-----------------------------------------------------------------------------------------------------
current_dir = Path.cwd()
parent_dir = current_dir.parent.parent
dir_path = parent_dir.joinpath("data")

#-----------------------------------------------------------------------------------------------------
# fetch a file
#-----------------------------------------------------------------------------------------------------
filename = "stock-price-data.csv"

filepath = dir_path.joinpath(filename)
ic(filepath)

stock_data = pd.read_csv(filepath)

ic(
    stock_data.head(),
    stock_data.columns,
    stock_data.dtypes,
    stock_data.index
)

#-----------------------------------------------------------------------------------------------------
# date fix?
#-----------------------------------------------------------------------------------------------------

stock_data["dt_as_pdDate"] = pd.to_datetime(
    stock_data["dt"],
    format = "%Y-%m-%d"
)

stock_data = stock_data.drop(columns="dt")

ic(
    stock_data.head(),
    stock_data.columns,
    stock_data.dtypes,
    stock_data.index
)

#-----------------------------------------------------------------------------------------------------
# Sort the dataframe by date (ascending)
# always be mindful to reset the index after sorting
# sorting syntax: df.sort_values(by=[<column-names>], ascending=[<True/False>]).reset_index(drop=True)
#-----------------------------------------------------------------------------------------------------

stock_data_sorted = stock_data.sort_values(
    by=["Symbol", "dt_as_pdDate"],
    ascending=[True, True]
).reset_index(drop=True)

ic(
    stock_data_sorted.head(),
    stock_data_sorted.columns,
    stock_data_sorted.dtypes
)

# Operations by group: compute daily returns and add as a new column
#-----------------------------------------------------------------------------------------------------
# Compute daily returns and add as a new column
# syntax: df['daily_return'] = df.groupby(['Symbol'])['adj_close'].pct_change(periods=N)
#-----------------------------------------------------------------------------------------------------

# version 1: using pct_change()

stock_data_sorted["return1day_v1"] = stock_data_sorted.groupby(
    ["Symbol"]
)["Close"].pct_change(periods=1)

ic(
    stock_data_sorted.head()
)

# version 2: using shift() and numpy divide

stock_data_sorted["lag_Close"] = stock_data_sorted.groupby(
    ["Symbol"]
)["Close"].shift(periods=1)

stock_data_sorted["return1day_v2"] = (
    stock_data_sorted["Close"] / stock_data_sorted["lag_Close"]
) - 1

ic(
    stock_data_sorted.head()
)

# how do I convert a column into a numpy array

arr1 = stock_data_sorted["return1day_v1"].to_numpy()
arr2 = stock_data_sorted["return1day_v2"].to_numpy()
ic(
    arr1, arr2
)

# check step

check = np.isclose(arr1, arr2, equal_nan=True).all()

ic(check)

#-----------------------------------------------------------------------

# only TSLA: conditional subset

subset_condition = stock_data_sorted["Symbol"].isin(["TSLA", "MMM"])

subset_condition1 = (
    stock_data_sorted["Symbol"] == "TSLA"
)

tsla_data_sorted = stock_data_sorted[subset_condition].reset_index(drop=True)

ic(
    tsla_data_sorted.head(n=20),
    tsla_data_sorted.index
)
