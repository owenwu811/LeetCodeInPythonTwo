#1715
#medium

#Write a solution to count the number of apples and oranges in all the boxes. If a box contains a chest, you should also include the number of apples and oranges it has.

#The result format is in the following example.

#my own solution using python3:

#follow the directions for chest or not chest and just total apples and oranges

import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    curapple, curorange = 0, 0
    for i, b in enumerate(boxes["chest_id"]):
        try:
            a = int(b)
            for j, v in enumerate(chests["chest_id"]):
                if v == b:
                    curapple += chests["apple_count"][j]
                    curorange += chests["orange_count"][j]
            curapple += boxes["apple_count"][i]
            curorange += boxes["orange_count"][i]
        except:
            curapple += boxes["apple_count"][i]
            curorange += boxes["orange_count"][i]
    print(curapple, curorange)
    res = pd.DataFrame()
    res["apple_count"] = [curapple]
    res["orange_count"] = [curorange]
    return res
