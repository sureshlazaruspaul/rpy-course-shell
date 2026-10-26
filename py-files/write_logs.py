# file: py/logging.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌

import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

list_seq = [1, 2, 3, 4, 5]
numpy_seq = np.array(list_seq)

logger.info(f"Converted list '{list_seq}' to numpy array '{numpy_seq}'.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
