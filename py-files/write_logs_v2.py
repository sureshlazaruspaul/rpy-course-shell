# type: ignore
# file: py/logging.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌ ❗

from pathlib import Path
import numpy as np 
import pandas as pd
import logging

# log package setup

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

logger.info("✅ Just a simple print statement")
logger.warning("⚠️ This is a WARNING")
logger.error("❌ DANGER: THIS IS AN ERROR")

class_size = 15

logger.info(
    f"✅ The number is {class_size}, the type of that variable is {type(class_size)}"
)
