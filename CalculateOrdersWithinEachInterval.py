#2893
#medium

#Write a query to calculate total orders within each interval. Each interval is defined as a combination of 6 minutes.

#Minutes 1 to 6 fall within interval 1, while minutes 7 to 12 belong to interval 2, and so forth.
#Return the result table ordered by interval_no in ascending order.

#The result format is in the following example.

#my own solution using python3:

#first map the original minutes to the original order count, and then sort the minutes, and then build the new order count according to the original mapped values in sorted order

import pandas as pd

def calculate_runs(orders: pd.DataFrame) -> pd.DataFrame:
    minutes = list(orders["minute"])
    d = dict()
    oc = list(orders["order_count"])
    for i, m in enumerate(minutes):
        d[m] = oc[i]
    print(d)
    minutes.sort()
    oc.clear()
    oc = [-1] * len(minutes)
    for i, m in enumerate(minutes):
        oc[i] = d[m]

    print(minutes)
    i = 0
    ans = []
    cnt = 1
    while i < len(minutes):
        cur = minutes[i: i + 6]
        now = oc[i: i + 6]
        ans.append([cnt, sum(now)])
        i += 6
        cnt += 1
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["interval_no"] = one
    res["total_orders"] = two
    return res
    
        #print(cur)
