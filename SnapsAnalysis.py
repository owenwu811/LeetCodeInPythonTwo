
#3056
#medium

#Write a solution to calculate the percentage of the total time spent on sending and opening snaps for each age group. Precentage should be rounded to 2 decimal places.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#use a dictionary of type list and subsitute the 1st element as send and 2nd as open

import pandas as pd

def snap_analysis(activities: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    for i, a in enumerate(age["age_bucket"]):
        d[age["user_id"][i]] = a
    dd = defaultdict(list)
    for i, a in enumerate(activities["user_id"]):
        if a not in dd:
            dd[d[a]] = [0, 0]
    for i, a in enumerate(activities["user_id"]):
        buc = d[a]
        if activities["activity_type"][i] == "send":
            dd[buc][1] += activities["time_spent"][i]
        elif activities["activity_type"][i] == "open":
            dd[buc][0] += activities["time_spent"][i]
    ans = []
    for k in dd:
        tot = sum(dd[k])
        sp = round(dd[k][0] / tot, 4) * 100
        op = round(dd[k][1] / tot, 4) * 100
        ans.append([k, op, sp])
    print(ans)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["age_bucket"] = one
    res["send_perc"] = two
    res["open_perc"] = three
    return res
