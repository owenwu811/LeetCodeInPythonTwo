#2884
#easy

#A company intends to give its employees a pay rise.

#Write a solution to modify the salary column by multiplying each salary by 2.

#The result format is in the following example.

#my own solution using python3:

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return pd.DataFrame(employees)
