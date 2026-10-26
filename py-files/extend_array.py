# file: extend_array.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

forecast_periods: int = 7
timestamp = np.array(range(1, forecast_periods + 1), dtype=float)

terminal_sales_growth_rate: float = 0.03

sales_array: np.ndarray = np.array([260174., 274515., 365817., 394328., 383285., 391035., 416161.])
lag_sales_array: np.ndarray = np.concatenate([[np.nan], sales_array[:-1]])

sales_growth_array: np.ndarray = np.subtract(np.divide(sales_array, lag_sales_array), 1)

# starting points for projections
mean_value: float = float(np.nanmean(sales_growth_array))
last_value: float = float(sales_growth_array[-1])

# growth philosophy
step: float = (terminal_sales_growth_rate - mean_value) / forecast_periods

#--- extending philospohy 1: using mean value as base and no step ---


#--- extending philospohy 2: using last value as base and no step ---


#--- extending philosophy 3: using mean value as base and step --- 


#--- extending philosophy 4: using last value as base and step ---


