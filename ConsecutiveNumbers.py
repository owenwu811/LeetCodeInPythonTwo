#180
#medium

#Find all numbers that appear at least three times consecutively.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#literally just use a list and sliding window of size 3 without duplicates

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, l in enumerate(logs["num"]):
        cur.append(l)
    ws = 3
    ans = []
    for i in range(len(cur) - 2):
        subarr = cur[i: i + ws]
        if len(set(subarr)) == 1:
            ans.append(subarr[0])
    print(ans)
    ans = list(set(ans))
    res = pd.DataFrame()
    res["ConsecutiveNums"] = ans
    return res
