# file: isinstance_check.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌

import logging
import pandas as pd
import numpy as np
from pathlib import Path
from icecream import ic

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import numpy as np
import pandas as pd
from pathlib import Path
