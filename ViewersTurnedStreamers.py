#2995
#Hard


#Write a solution to find the number of streaming sessions for users whose first session was as a viewer.

#Return the result table ordered by count of streaming sessions,  user_id in descending order.

#The result format is in the following example.


#my own solution using python3:

#sort by the session start times, and then iterate through each key, fulfilling the requirements, and then sort the list by session count and then user id in reverse order, and then populate the dataframe

import pandas as pd

def count_turned_streamers(sessions: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, u in enumerate(sessions["user_id"]):
        d[u].append([sessions["session_start"][i], sessions["session_type"][i]])
        d[u].sort()
    ans = []
    for k in d:
        if d[k][0][-1] == "Viewer":
            #print(k, d[k])
            cnt = 0
            for a in d[k][1:]:
                if a[-1] == "Streamer":
                    cnt += 1
            if cnt > 0:
                print(k, cnt)
                ans.append([k, cnt])
    ans.sort(key=lambda x: (x[1], x[0]), reverse=True)
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["user_id"] = one
    res["sessions_count"] = two
    return res
