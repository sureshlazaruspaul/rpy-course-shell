# type: ignore

import time
import yfinance as yf
from icecream import ic
import pandas as pd
import numpy as np
from pathlib import Path
from plyer import notification


notification.notify(
    title="message title",
    message="hi! How r u?"
)











# file = "https://docs.google.com/spreadsheets/d/{sheet_id}/edit?usp=sharing"

sheet_id = "enter sheet id here"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"



