# import packages

import pandas as pd
import numpy as np
from icecream import ic
from pathlib import Path

# import csv file using pathlib

file_path = Path.cwd().parent.joinpath("data", "amzn_stock_price.csv")

amzn_data = pd.read_csv(file_path)

# ic(amzn_data.head(), amzn_data.dtypes)

# convert str/object to a pandas date object
date_as_pdDate = pd.to_datetime(amzn_data["date"])
# ic(date_as_pdDate)

# create a variable in dataframe

# amzn_data["date_as_pdDate"] = date_as_pdDate

# or

# date formats

date1 = "03-15-1997" # "%m-%d-%Y"

date1_as_pdDate = pd.to_datetime(date1, format="%m-%d-%Y")
# ic(date1_as_pdDate)


date1a = "03-15-97" # "%m-%d-%y"

date1a_as_pdDate = pd.to_datetime(date1a, format="%m-%d-%y")
# ic(date1a_as_pdDate)

date2 = "03 Jan 2002" # "%d %b %Y"

date2_as_pdDate = pd.to_datetime(date2, format="%d %b %Y")
# ic(date2_as_pdDate)


date3 = "January 23 2012" # "%B %d %Y"

date3_as_pdDate = pd.to_datetime(date3, format="%B %d %Y")
# ic(date3_as_pdDate)


date4 = "19861231" # "%Y%m%d"

date4_as_pdDate = pd.to_datetime(date4, format="%Y%m%d")
# ic(date4_as_pdDate)


amzn_data["date1_as_pdDate"] = pd.to_datetime(amzn_data["date"], format="%Y-%m-%d")

# ic(amzn_data.head(), amzn_data.dtypes)

# Date Manipulations
# 1. Add to the date

# using DateOffset
# amzn_data["next_date"] = amzn_data["date1_as_pdDate"] + pd.DateOffset(months=-5)
# ic(amzn_data.head(), amzn_data.dtypes)

# using TimeDelta
# amzn_data["twodays_later"] = amzn_data["date1_as_pdDate"] + pd.Timedelta(days=2)
# ic(amzn_data.head(), amzn_data.dtypes)

# date difference

todays_date = pd.to_datetime("2026-11-02", format="%Y-%m-%d")

# amzn_data["diff_date"] = amzn_data["date1_as_pdDate"] - todays_date
# ic(amzn_data.head(), amzn_data.dtypes)

# date specifics
# 1. Extract Year

# amzn_data["year"] = amzn_data["date1_as_pdDate"].dt.year
# amzn_data["month"] = amzn_data["date1_as_pdDate"].dt.month
# amzn_data["day"] = amzn_data["date1_as_pdDate"].dt.day
# amzn_data["day_of_week"] = amzn_data["date1_as_pdDate"].dt.day_of_week
# amzn_data["dayname"] = amzn_data["date1_as_pdDate"].dt.day_name()
# ic(amzn_data.head(), amzn_data.dtypes)

# variable treatments conditionally

# 1. Column T/F based a criteria
# True if number greater than a specific number, False otherwise

# amzn_data["gt8cents"] = amzn_data["low_price"] > 0.0800
# ic(amzn_data.head(n=25), amzn_data.dtypes)

# amzn_data["tues_thurs_only"] = amzn_data["dayname"].isin(["Tuesday", "Thursday"])

# amzn_data["Wed_only"] = amzn_data["dayname"] == "Wednesday"
# ic(amzn_data.head(n=25))

# 2. Column Text based on a criteria

# amzn_data["wednesday_only"] = np.where(amzn_data["dayname"] == "Wednesday", "Use this", "Ignore this")
# ic(amzn_data.head(n=25))

# 3. drop missing values

# a) lag adj close
# Step 1: sort the data by date
# Step 2: Compute lag

amzn_data = amzn_data.sort_values(by=["date1_as_pdDate"], ascending=[True])
amzn_data["lag_adj_close"] = amzn_data["adj_close"].shift(periods=1)

amzn_data["return1day"] = (amzn_data["adj_close"]/amzn_data["lag_adj_close"]) - 1

# using perc change
amzn_data["return1day_v1"] = amzn_data["adj_close"].pct_change(periods=1)
# ic(amzn_data.head(n=25))

amzn_data_v1 = amzn_data.dropna(subset=["lag_adj_close"])


# 4. keep some variables
# keep pd date, adj_close, return 1 

# amzn_data_v2 = amzn_data_v1[["date1_as_pdDate", "adj_close", "return1day_v1"]]


keep_list = ["date1_as_pdDate", "adj_close", "return1day_v1"]
amzn_data_v2 = amzn_data_v1[keep_list]
# ic(keep_list, amzn_data_v2.head(n=5))

# 5. drop some variables

# amzn_data_v3 = amzn_data.drop(columns=["open_price", "high_price"])
# ic(amzn_data_v3.head(n=5))

drop_list = ["open_price", "high_price", "volume", "date"]

amzn_data_v3 = amzn_data.drop(columns=drop_list).dropna(subset=["lag_adj_close"])
ic(amzn_data_v3.head(n=5))

ic(
    np.isclose(
        amzn_data_v3["return1day"],
        amzn_data_v3["return1day_v1"]
    ).all()
)