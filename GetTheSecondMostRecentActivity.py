#1369
#Hard

#Write a solution to show the second most recent activity of each user.

#If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#group by the name and then sort each list by the start and end dates

import pandas as pd

def second_most_recent(user_activity: pd.DataFrame) -> pd.DataFrame:
    cur = []
    d = defaultdict(list)
    for i, v in enumerate(user_activity["username"]):
        d[v].append([user_activity["startDate"][i], user_activity["endDate"][i], user_activity["activity"][i]])
        d[v].sort()
    cnt = 0
    for k in d:
        if len(d[k]) >= 2:
            #print(k, d[k][-2])
            now = d[k][-2]
            s = str(now[0]).split(" ")
            e = str(now[1]).split(" ")
            s = s[0]
            e = e[0]
            print(s, e)
            user_activity["username"][cnt] = k
            user_activity["activity"][cnt] = now[2]
            user_activity["startDate"][cnt] = s
            user_activity["endDate"][cnt] = e
            cnt += 1

        else:
            now = d[k][-1]
            s = str(now[0]).split(" ")
            e = str(now[1]).split(" ")
            s = s[0]
            e = e[0]
            print(s, e)
            user_activity["username"][cnt] = k
            user_activity["activity"][cnt] = now[2]
            user_activity["startDate"][cnt] = s
            user_activity["endDate"][cnt] = e
            cnt += 1

    return pd.DataFrame(user_activity, columns=["username", "activity", "startDate", "endDate"]).head(len(d))
