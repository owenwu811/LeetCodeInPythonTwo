#176
#medium

#Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

#The result format is in the following example.

#my own solution using python3:

#just use a set, sort the list, and get the 2nd to last

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, e in enumerate(employee["salary"]):
        cur.append(e)
    cur = list(set(cur))
    cur.sort()
    print(cur)
    res = pd.DataFrame(columns=["SecondHighestSalary"])
    if len(cur) < 2:
        cur = [None]
        res["SecondHighestSalary"] = cur
    else:
        cur = [cur[-2]]
        print(cur)
        res["SecondHighestSalary"] = cur
    return res
