#2228
#medium

#Write a solution to report the IDs of the users that made any two purchases at most 7 days apart.

#Return the result table ordered by user_id.

#The result format is in the following example.

#my own solution using python3:

#get all the purchase dates for each user id, and see if any <= 7 to include in ans

import pandas as pd

def find_valid_users(purchases: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, p in enumerate(purchases["purchase_date"]):
        #if purchases["user_id"][i] != purchases["purchase_id"][i]:
        d[purchases["user_id"][i]].append(p)
        d[purchases["user_id"][i]].sort()
    ans = []
    for k in d:
        #flag = True
        if len(d[k]) > 1:
            print(k, d[k])
            flag = True
            for j in range(1, len(d[k])):
                diff = d[k][j] - d[k][j - 1]
                now = str(diff).split(" ")[0]
                if int(now) <= 7:
                    ans.append(k)
                    ans.sort()
                    break
    res = pd.DataFrame()
    res["user_id"] = ans
    return res
