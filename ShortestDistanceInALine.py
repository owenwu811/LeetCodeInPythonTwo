#613
#easy

#Find the shortest distance between any two points from the Point table.

#The result format is in the following example.

#my own solution using python3:

#just sort the values and go one by one

import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for v in point["x"]:
        cur.append(v)
    cur.sort()
    print(cur)
    ans = float('inf')
    for i in range(1, len(cur)):
        ans = min(ans, abs(cur[i] + cur[i - 1]), abs(cur[i] - cur[i - 1]))
    print(ans)
    res = pd.DataFrame()
    res["shortest"] = [ans]
    return res
