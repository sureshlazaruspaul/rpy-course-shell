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
filename1 = "tsla_stock_price.csv"
filename2 = "stock-price-data.csv"
file_fullpath1 = dir_path.joinpath(filename1)
file_fullpath2 = dir_path.joinpath(filename2)
ic(file_fullpath1, file_fullpath2)

tsla_stock_data_df = pd.read_csv(file_fullpath1)
ic(tsla_stock_data_df.head(), tsla_stock_data_df.dtypes, tsla_stock_data_df.shape, tsla_stock_data_df.columns)

#-----------------------------------------------------------------------------------------------------
# Sort the dataframe by date (ascending)
# always be mindful to reset the index after sorting
# sorting syntax: df.sort_values(by=[<column-names>], ascending=[<True/False>]).reset_index(drop=True)
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
# Compute daily returns and add as a new column
# syntax: df['daily_return'] = df['adj_close'].pct_change(periods=N)
#-----------------------------------------------------------------------------------------------------

# version 1: using pct_change()
# version 2: using shift()
# check if both versions are equal using np.isclose()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# fetch another file
#-----------------------------------------------------------------------------------------------------

stock_data_df = pd.read_csv(file_fullpath2)
ic(stock_data_df.head(), stock_data_df.dtypes, stock_data_df.shape, stock_data_df.columns)

#-----------------------------------------------------------------------------------------------------
# Sort the dataframe by date (ascending)
# always be mindful to reset the index after sorting
# sorting syntax: df.sort_values(by=[<column-names>], ascending=[<True/False>]).reset_index(drop=True)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# Compute daily returns and add as a new column
# syntax: df['daily_return'] = df.groupby(['Symbol'])['adj_close'].pct_change(periods=N)
#-----------------------------------------------------------------------------------------------------

# version 1: using pct_change()
# version 2: using shift()
# check if both versions are equal using np.isclose()
