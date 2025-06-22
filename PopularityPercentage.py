
#2720
#hard

#Write a solution to find the popularity percentage for each user on Meta/Facebook. The popularity percentage is defined as the total number of friends the user has divided by the total number of users on the platform, then converted into a percentage by multiplying by 100, rounded to 2 decimal places.

#Return the result table ordered by user1 in ascending order.

#The result format is in the following example.

#my own solution using python3:

#easy except fill the result with all the values, not just user1

import pandas as pd

def popularity_percentage(friends: pd.DataFrame) -> pd.DataFrame:
    tot = set()
    for i, v in enumerate(friends["user1"]):
        tot.add(v)
    for i, v in enumerate(friends["user2"]):
        tot.add(v)
    print(tot)
    d = defaultdict(set)
    for i, v in enumerate(friends["user1"]):
        d[v].add(friends["user2"][i])
        d[friends["user2"][i]].add(v)
    ans = []
    for k in d:
        val = (len(d[k]) / len(tot)) * 100
        val = round(val, 2)
        ans.append([k, val])
    ans.sort()
    print(ans)

    res = pd.DataFrame()
    res["user1"] = list(tot)
    res["percentage_popularity"] = 0.0
    cnt = 0
    for a in ans:
        res["user1"][cnt] = a[0]
        res["percentage_popularity"][cnt] = a[1]
        cnt += 1
    
    

    return pd.DataFrame(res, columns=["user1", "percentage_popularity"]).head(len(ans))
