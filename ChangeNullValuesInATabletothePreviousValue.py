#2388
#medium

#Write a solution to replace the null values of the drink with the name of the drink of the previous row that is not null. It is guaranteed that the drink on the first row of the table is not null.

#Return the result table in the same order as the input.

#The result format is shown in the following example.

#my own solution using python3:

#if it's null, then look at the value at top of stack and use that value; otherwise, keep appending to rear of stack

import pandas as pd

def change_null_values(coffee_shop: pd.DataFrame) -> pd.DataFrame:
    cur = []
    used = []
    for i, c in enumerate(coffee_shop["drink"]):
        try:
            a = len(c)
            print(c)
            cur.append(c)
            used.append(c)
        except:
            print(used)
            cur.append(used[-1])
    one, two = [], []
    for i, c in enumerate(coffee_shop["id"]):
        one.append(c)
    two = cur
    print(one, two)
    res = pd.DataFrame()
    res["id"] = one
    res["drink"] = two
    return res
