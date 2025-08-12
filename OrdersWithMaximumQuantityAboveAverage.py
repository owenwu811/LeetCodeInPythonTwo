#1867
#medium

#You are running an e-commerce site that is looking for imbalanced orders. An imbalanced order is one whose maximum quantity is strictly greater than the average quantity of every order (including itself).

#The average quantity of an order is calculated as (total quantity of all products in the order) / (number of different products in the order). The maximum quantity of an order is the highest quantity of any single product in the order.

#Write a solution to find the order_id of all imbalanced orders.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#find the averages, and then get the biggest of each to compare with the biggest of the averages

import pandas as pd

def orders_above_average(orders_details: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    avg = dict()
    for i, o in enumerate(orders_details["order_id"]):
        d[o].append(orders_details["quantity"][i])
    for k in d:
        avg[k] = round(sum(d[k]) / len(d[k]), 2)
    #print(avg)
    cur = list(avg.values())
    cur.sort()
    ans = []
    for k in d:
        if max(d[k]) > cur[-1]:
            print(k)
            ans.append(k)
    res = pd.DataFrame()
    res["order_id"] = ans
    return res
