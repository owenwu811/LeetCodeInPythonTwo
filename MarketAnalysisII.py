#1159
#Hard

#Write a solution to find for each user whether the brand of the second item (by date) they sold is their favorite brand. If a user sold less than two items, report the answer for that user as no. It is guaranteed that no seller sells more than one item in a day.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#get all the users and all their transactions by order date and item id, and sort it by order date, and then try to match up to the rules

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    fav = dict()
    ite = defaultdict(str)
    for i, u in enumerate(users["user_id"]):
        fav[u] = users["favorite_brand"][i]
    for i, u in enumerate(items["item_id"]):
        ite[u] = items["item_brand"][i]
    for i, o in enumerate(orders["seller_id"]):
        d[o].append([orders["order_date"][i], orders["item_id"][i]])
        d[o].sort(key=lambda x: x[0])
    userids = list(users["user_id"])
    ans = []
    for u in userids:
        if u not in d:
            ans.append([u, "no"])
    for k in d:
        if len(d[k]) < 2:
            ans.append([k, "no"])
        else:
            print(k, d[k])
            if fav[k] == ite[d[k][1][1]]:
                ans.append([k, "yes"])
            else:
                ans.append([k, "no"])
        
    #print(ans)
    ans.sort()

    one, two = [], []
    for a in ans: 
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["seller_id"] = one
    res["2nd_item_fav_brand"] = two
    return res
