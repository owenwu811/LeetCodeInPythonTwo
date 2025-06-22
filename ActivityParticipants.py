#1355
#medium

#Find the names of all the activities with neither the maximum nor the minimum number of participants.

#Each activity in the Activities table is performed by any person in the table Friends.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#just follow the instructions

import pandas as pd

def activity_participants(friends: pd.DataFrame, activities: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, f in enumerate(friends["activity"]):
        d[f] += 1
    print(d)
    small = min(d.values())
    large = max(d.values())
    ans = []
    for k in d:
        if d[k] != small and d[k] != large:
            print(k)
            ans.append(k)
    res = pd.DataFrame(columns=["activity"])
    res["activity"] = friends["activity"]
    cnt = 0
    for a in ans:
        res["activity"][cnt] = ans[cnt]
        cnt += 1

    return res.head(len(ans))
