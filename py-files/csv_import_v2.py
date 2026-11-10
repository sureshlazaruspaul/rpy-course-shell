# import packages first
import pandas as pd
import numpy as np
from icecream import ic 
from pathlib import Path

# what is the current directory?

current_dir = Path.cwd()
ic(current_dir)

# one up folder

one_up_dir = current_dir.parent
ic(one_up_dir)

# data folder

data_dir = one_up_dir.joinpath("data")
ic(data_dir)

# file path

file_path = data_dir.joinpath("mtcars.csv")
ic(file_path)

# import csv file
# pd.read_csv()

mtcars_data = pd.read_csv(file_path)
ic(mtcars_data)

iris_data = pd.read_csv(data_dir.joinpath("iris.csv"))
ic(iris_data)

aapl_data = pd.read_csv(
    Path.cwd().parent.joinpath("data", "aapl_stock_price.csv")
)
ic(aapl_data)

dates_data = pd.read_csv("https://raw.githubusercontent.com/sureshlazaruspaul/rpy-course-shell/refs/heads/main/data-files/dates.csv")
ic(dates_data)


# preview first few rows

print(
    mtcars_data.head(n=15)
)

# preview last few lines

ic(
    iris_data.tail(n=20)
)

# shape of data

ic(dates_data.shape)

# column names in data

ic(aapl_data.columns)

# describe the data

ic(iris_data.describe())

# index of data

ic(
    dates_data.index
)

# data types of variables in data

ic(
    aapl_data.dtypes
)

# save a csv to specific folder
# C:\PyProg\data\save_here
# which file? mtcars.csv
# file_path_saved: C:\PyProg\data\save_here\mtcars.csv

file_path_saved = "C:\PyProg\data\save_here\mtcars.csv"

mtcars_data.to_csv(file_path_saved, index=True)

# or
# mtcars_data.to_csv("C:\PyProg\data\save_here\mtcars.csv", index=False)


# relative path using Path to save a file
# data_dir

file_path_saved2 = data_dir.joinpath("random_folder", "python_folder", "McLaren.csv")

mtcars_data.to_csv(file_path_saved2, index=False)