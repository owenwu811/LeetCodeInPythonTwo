
#1613
#medium

#Write a solution to find the missing customer IDs. The missing IDs are ones that are not in the Customers table but are in the range between 1 and the maximum customer_id present in the table.

#Notice that the maximum customer_id will not exceed 100.

#Return the result table ordered by ids in ascending order.

#The result format is in the following example.

#my own solution using python3:

#just get everything, and then use a key from 1 to biggest, and see what's missing, and then sort that

import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, c in enumerate(customers["customer_id"]):
        cur.append(c)
    cur.sort()
    smal, larg = min(cur), max(cur)
    key = list(range(1, larg + 1))
    print(cur)
    print(key)
    ans = []
    for k in key:
        if k not in cur:
            ans.append(k)
    ans.sort()
    res = pd.DataFrame()
    res["ids"] = ans
    return res
