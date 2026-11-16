# file: if_loops_basics.py
# add emoticons to logging messages for quick diagnosis
# Example usage: success: ✅, warning: ⚠️, error: ❌, processing: ⚙️

import logging
from icecream import ic
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

#-SAMPLE DATA-----------------------------------------------------------------------------------------------------

score: int = 75
attendance: bool = True
homework: float = 90.76

scores_list: List[int] = [85, 92, 78, 64, 88, 73, 95, 67, 81, 59, 90, 76, 84, 46, 91, 82, 77, 60, 89, 94, 25]
age_list: List[int] = [3, 17, 25, 70, 15, 45, 80, 12, 33, 66, 5, 90, 18, 55, 40, 2, 77, 29, 60, 11]

#-----------------------------------------------------------------------------------------------------------------
# loops concepts
# if statements: if, elif, else
#   if score greater than 70, attendance meets requirements, and homework score is greater than 90, then PASS
#   if score greater than 70, attendance meets requirements, and homework score is less than 90, then EXTENSION
#   otherwise, FAIL
#-----------------------------------------------------------------------------------------------------------------




# did you pass?



# detailed report: did you pass?




#-----------------------------------------------------------------------------------------------------------------
# what grade?
# - above 90 is A, 80 -- 90 is B, 70 -- 80 is C, 60 -- 70 is D, < 60 is F
#-----------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------
# use of breaks and continue
# did anyone fail?
#-----------------------------------------------------------------------------------------------------------------
# STOP at first instance with break




# Get every fitting data with continue




#-----------------------------------------------------------------------------------------------------------------
# discrete conditional checks to create a new list
#-----------------------------------------------------------------------------------------------------------------



