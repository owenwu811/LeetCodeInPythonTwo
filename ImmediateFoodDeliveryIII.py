#2686
#medium

#If the customer's preferred delivery date is the same as the order date, then the order is called immediate, otherwise, it is scheduled.

#Write a solution to find the percentage of immediate orders on each unique order_date, rounded to 2 decimal places. 

#Return the result table ordered by order_date in ascending order.

#The result format is in the following example.


#my own solution using python3:

#track the percentages of i and s for each key, and sort the final results as asked

import pandas as pd

def immediate_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(delivery["order_date"]):
        cur = cur = str(v).split(" ")[0]
        if v == delivery["customer_pref_delivery_date"][i]:
            d[cur].append("i")
        else:
            d[cur].append("s")
    ans = dict()
    for k in d:
        perc = round(d[k].count("i") / len(d[k]) * 100, 2)
        ans[k] = perc
    f = []
    for a in ans:
        f.append([a, ans[a]])
    f.sort(key=lambda x: x[0])
    print(f)
    one, two = [], []
    for y in f:
        one.append(y[0])
        two.append(y[1])
    res = pd.DataFrame()
    res["order_date"] = one
    res["immediate_percentage"] = two
    return res
        
