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


#-----------------------------------------------------------------------------------------------------
# date fix?
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
# Sort the dataframe by date (ascending)
# always be mindful to reset the index after sorting
# sorting syntax: df.sort_values(by=[<column-names>], ascending=[<True/False>]).reset_index(drop=True)
#-----------------------------------------------------------------------------------------------------


# Operations by group: compute daily returns and add as a new column
#-----------------------------------------------------------------------------------------------------
# Compute daily returns and add as a new column
# syntax: df['daily_return'] = df.groupby(['Symbol'])['adj_close'].pct_change(periods=N)
#-----------------------------------------------------------------------------------------------------

# version 1: using pct_change()


# version 2: using shift() and numpy divide


#-----------------------------------------------------------------------

# only TSLA:
