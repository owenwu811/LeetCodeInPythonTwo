#177
#medium


#Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

#The result format is in the following example.

#my own solution using python3:

#use the variable integer as a string in the resulting column name

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    cur = []
    for i, e in enumerate(employee["salary"]):
        cur.append(e)
    cur = list(set(cur))
    cur = sorted(cur)
    res = pd.DataFrame()
    if len(cur) < N or N <= 0:
        cur = [None]
        param = N
        columnname = "getNthHighestSalary" + "(" + str(param) + ")"
        res[columnname] = cur
    else:
        cur = [cur[-N]]
        param = N
        columnname = "getNthHighestSalary" + "(" + str(param) + ")"
        res[columnname] = cur
    return res
