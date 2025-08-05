#3220
#medium

#Write a solution to find the sum of amounts for odd and even transactions for each day. If there are no odd or even transactions for a specific date, display as 0.

#Return the result table ordered by transaction_date in ascending order.

#The result format is in the following example.

#my own solution using python3:

#use dictionaries to track the odd and even sums for each day, and then fill in missing keys for all dates in all dictionaries with 0, and then sort by date

import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    ed, od = defaultdict(int), defaultdict(int)
    dates = set()
    for i, t in enumerate(transactions["transaction_date"]):
        cur = str(t).split(" ")[0]
        dates.add(cur)
        if transactions["amount"][i] % 2 == 0:
            ed[cur] += transactions["amount"][i]
        else:
            od[cur] += transactions["amount"][i]
    #print(ed, od)
    for d in dates:
        if d not in ed:
            ed[d] = 0
        if d not in od:
            od[d] = 0
    #print(ed, od)
    ans = []
    for e in ed:
        ans.append([e, od[e], ed[e]])
    print(ans)
    ans.sort(key=lambda x: x[0])
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["transaction_date"] = one
    res["odd_sum"] = two
    res["even_sum"] = three
    return res


