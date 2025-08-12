#534
#medium

#Write a solution to report for each player and date, how many games played so far by the player. That is, the total number of games played by the player until that date. Check the example for clarity.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#order by the date, and then segment by each player id, and use prefix sums to get each entry

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    cur = []
    d = defaultdict(list)
    for i, a in enumerate(activity["event_date"]):
        cur.append([a, activity["player_id"][i], activity["device_id"][i], activity["games_played"][i]])
    #print(cur)
    for c in cur:
        d[c[1]].append([c[0], c[2], c[3]])
        d[c[1]].sort(key=lambda x: x[0])
    ans = []
    for k in d:
        #print(k, d[k])
        now = 0
        for a in d[k]:
            now += a[-1]
            ans.append([k, str(a[0]).split(' ')[0], now])
    print(ans)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["player_id"] = one
    res["event_date"] = two
    res["games_played_so_far"] = three
    return res
