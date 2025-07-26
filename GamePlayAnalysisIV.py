#550
#medium

#Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

#The result format is in the following example.

#my own solution using python3:

#gather the 1st time of each player, and then check the 1st and 2nd times to make sure difference is exactly 1 day

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first = defaultdict(list)
    totu = set()
    for i, a in enumerate(activity["player_id"]):
        totu.add(a)
        first[a].append(activity["event_date"][i])
        first[a].sort()
    tag = set()
    for f in first:
        if len(first[f]) > 1:
            print(f, first[f][:2])
            if int(str(first[f][1] - first[f][0]).split(" ")[0]) == 1:
                print(f)
                tag.add(f)
            
    #print(tag, totu)
    res = pd.DataFrame()
    res["fraction"] = [round(len(tag) / len(totu), 2)]
    return res
