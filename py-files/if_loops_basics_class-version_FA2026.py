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

score: int = 50
attendance: bool = True
homework: float = 85.3

scores_list: List[int] = [85, 92, 78, 64, 88, 73, 95, 67, 81, 59, 90, 76, 84, 46, 91, 82, 77, 60, 89, 94, 25]
age_list: List[int] = [3, 17, 25, 70, 15, 45, 80, 12, 33, 66, 5, 90, 18, 55, 40, 2, 77, 29, 60, 11]

#-----------------------------------------------------------------------------------------------------------------
# loops concepts
# if statements: if, elif, else
#   if score greater than 70, attendance meets requirements, and homework score is greater than 90, then PASS
#   if score greater than 70, attendance meets requirements, and homework score is less than 90, then EXTENSION
#   otherwise, FAIL
#-----------------------------------------------------------------------------------------------------------------

pass_condition: bool = (
    (score > 70) and 
    (attendance is True) and 
    (homework > 90)
)

ic(pass_condition)

extension_condition = (
    (score > 70) and (attendance == True) and 
    (homework < 90)
)

ic(extension_condition)


# did you pass?

if pass_condition == True:
    logger.info("✅ You passed.")


# detailed report: did you pass?

if pass_condition == True:
    logger.info("✅ You passed.")
elif extension_condition == True:
    logger.info("⚠️ You secured an extension.")
else:
    logger.info("❌ You failed the course.")


#-----------------------------------------------------------------------------------------------------------------
# what grade?
# - above 90 is A, 80 -- 90 is B, 70 -- 80 is C, 60 -- 70 is D, < 60 is F
#-----------------------------------------------------------------------------------------------------------------

scores_list: List[int] = [85, 92, 78, 64, 88, 73, 95, 67, 81, 59, 90, 76, 84, 46, 91, 82, 77, 60, 89, 94, 25]

letter_grades: List[str] = []

for each_score in scores_list:
    if each_score > 90:
        letter_grades.append("A")
    elif each_score > 80:
        letter_grades.append("B")
    elif each_score > 70:
        letter_grades.append("C")
    elif each_score >= 60:
        letter_grades.append("D")
    else:
        letter_grades.append("F")

for score, grade in zip(scores_list, letter_grades):
    logger.info(f"{score=}, {grade=}")

#-----------------------------------------------------------------------------------------------------------------
# use of breaks and continue
# did anyone fail?
#-----------------------------------------------------------------------------------------------------------------
# STOP at first instance with break

for score in scores_list:
    ic(score)
    if score < 60:
        logger.info(f"❌ Someone failed the course.")
        break


# Get every fitting data with continue

scores_list: List[int] = [85, 92, 78, 64, 88, 73, 95, 67, 81, 59, 90, 76, 84, 46, 91, 82, 77, 60, 89, 94, 25]

for score in scores_list:
    ic(score)
    if score >= 60:
        continue
    # if score > 60, 
    # nothing downstream after continue is executed
    logger.info("❌ Someone failed the course.")

#-----------------------------------------------------------------------------------------------------------------
# discrete conditional checks to create a new list
#-----------------------------------------------------------------------------------------------------------------

new_grades_list: List[str] = []

for values in scores_list:
    
    if values > 90:
        new_grades_list.append("A")

    if values > 80 and values <= 90:
        new_grades_list.append("B")

    if values > 70 and values <= 80:
        new_grades_list.append("C")

    if values >= 60 and values <= 70:
        new_grades_list.append("D")

    if values < 60:
        new_grades_list.append("F")

for value, letter, new_letter in zip(scores_list, letter_grades, new_grades_list):
    logger.info(f"{value=}, {letter=}, {new_letter=}")