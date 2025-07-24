
#2494
#Hard

#Write a solution to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#gather all the start and end dates for each hall id, and then sort all the dates, and then merge them 

import pandas as pd

def merge_events(hall_events: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, h in enumerate(hall_events["hall_id"]):
        s, e = str(hall_events["start_day"][i]).split(" ")[0], str(hall_events["end_day"][i]).split(" ")[0]
        
        d[h].append([s, e])
        d[h].sort()

    dd = defaultdict(list)
    one, two, three = [], [], []
    for k in d:
        print(k, d[k])
        cur = [d[k][0]]
        #print(cur)
        now = d[k]
        for j in range(1, len(now)):
            if now[j][0] <= cur[-1][-1]:
                cur[-1][-1] = max(cur[-1][-1], now[j][1])
            else:
                cur.append(now[j])
        print(cur)
        dd[k] = cur.copy()
    for k in dd:
        for a in dd[k]:
            one.append(k)
            two.append(a[0])
            three.append(a[1])
    res = pd.DataFrame()
    res["hall_id"] = one
    res["start_day"] = two
    res["end_day"] = three
    return res

