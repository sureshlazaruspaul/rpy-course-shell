# file: csv_import.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌

import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

abs_path = Path("C:\\data\\iris.csv")
if abs_path.exists():
    print("File exists.")
else:
    print("File does not exist.")

df = pd.read_csv(abs_path)
