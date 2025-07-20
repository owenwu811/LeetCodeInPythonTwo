#2986
#medium

#Write a solution to find the third transaction (if they have at least three transactions) of every user, where the spending on the preceding two transactions is lower than the spending on the third transaction.

#Return the result table by user_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#gather all the transaction dates and spend amounts for each uid, and then sort those by the transaction dates, and then compare the 3rd to 1st and 2nd

import pandas as pd

def find_third_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, t in enumerate(transactions["user_id"]):
        d[t].append([transactions["transaction_date"][i], transactions["spend"][i]])
        d[t].sort(key=lambda x: x[0])
    ans = []
    for k in d:
        if len(d[k]) >= 3:
            print(k, d[k])
            if d[k][0][1] < d[k][2][1] and d[k][1][1] < d[k][2][1]:
            #print(k, d[k][2][1], d[k][2][0])
                ans.append([k, d[k][2][1], d[k][2][0]])
    ans.sort()
    o, t, th = [], [], []
    for a in ans:
        o.append(a[0])
        t.append(a[1])
        th.append(a[2])
    res = pd.DataFrame()
    res["user_id"] = o
    res["third_transaction_spend"] = t
    res["third_transaction_date"] = th
    return res
