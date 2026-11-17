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
# fetch a file + direct import from online
#-----------------------------------------------------------------------------------------------------
filename = "https://raw.githubusercontent.com/sureshlazaruspaul/rpy-course-shell/refs/heads/main/data-files/sp500_prices.csv"

sp500_data = pd.read_csv(filename)

ic(
    sp500_data.head(),
    sp500_data.columns,
    sp500_data.dtypes,
    sp500_data.index
)

#-----------------------------------------------------------------------------------------------------
# date fix?
#-----------------------------------------------------------------------------------------------------

sp500_data["date_as_pdDate"] = pd.to_datetime(
    sp500_data["date"],
    format = "%Y-%m-%d"
)

# clean-up

keepvars = ["symbol", "date_as_pdDate", "adjusted"]

sp500_data = sp500_data[keepvars]

#-----------------------------------------------------------------------------------------------------
# fetch year from date and add as a new column
#-----------------------------------------------------------------------------------------------------

sp500_data["year"] = sp500_data["date_as_pdDate"].dt.year

ic(
    sp500_data.head(),
    sp500_data.columns,
    sp500_data.dtypes,
    sp500_data.index
)



#-----------------------------------------------------------------------------------------------------
# transform the dataframe using agg function() by group:
# - "mean", "sum", "count", "min", "max", "first", "last"
# - syntax: .groupby(["symbol", "year"]).agg(varname=("column", "aggregation")).reset_index()
#-----------------------------------------------------------------------------------------------------

# 1. Get all aggregations for each symbol and year

sp500_data_annualized = sp500_data.groupby(
    ["symbol", "year"]
).agg(
    mean_price = ("adjusted", "mean"),
    sum_price = ("adjusted", "sum"),
    count_price = ("adjusted", "count"),
    min_price = ("adjusted", "min"),
    max_price = ("adjusted", "max"),
    first_price = ("adjusted", "first"),
    last_price = ("adjusted", "last")
)

sp500_data_annualized["annual_ret"] = (
    sp500_data_annualized["last_price"] / sp500_data_annualized["first_price"]
) - 1

ic(sp500_data_annualized.head(n=100))

# compute mean
average_return = sp500_data_annualized["annual_ret"].mean()

ic(average_return)

sp500_data_annualized.to_csv(dir_path.joinpath("sp500_data_annualized.csv"))