#1158
#medium

#Write a solution to find for each user, the join date and the number of orders they made as a buyer in 2019.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#use two dictionaries to track the join date and then the 2019 buyer frequencies, and then merge them at the end

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    for i, u in enumerate(users["user_id"]):
        d[u] = users["join_date"][i]
    dd = defaultdict(int)
    for i, o in enumerate(orders["order_date"]):
        cur = str(o).split(" ")[0][:4]
        if cur == "2019":
            dd[orders["buyer_id"][i]] += 1
    for k in d:
        if k not in dd:
            dd[k] = 0
    print(dd)
    one, two, three, = [], [], []
    for k in dd:
        one.append(k)
        two.append(d[k])
        three.append(dd[k])
    res = pd.DataFrame()
    res["buyer_id"] = one
    res["join_date"] = two
    res["orders_in_2019"] = three
    return res
