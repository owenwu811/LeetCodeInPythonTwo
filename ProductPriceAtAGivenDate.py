#1164
#medium

#Initially, all products have price 10.

#Write a solution to find the prices of all products on the date 2019-08-16.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#sort by the change date, and then gather the right most index that is august 16 2019, and then find the rightmost of each of the product ids prices

import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    cur = []
    now = []
    tot = set()
    for i, p in enumerate(products["change_date"]):
        tot.add(products["product_id"][i])
        cur.append([p, products["product_id"][i], products["new_price"][i]])
    cur.sort(key=lambda x: x[0])
    biggest = 0
    for i, c in enumerate(cur):
        if str(c[0]).split(" ")[0] == "2019-08-16":
            biggest = max(biggest, i)
            #val = cur[:i + 1]
            #break
    val = cur[:biggest + 1]
    print(val)
    d = defaultdict(list)
    for i, v in enumerate(val):
        d[v[1]].append(v[2])
    ans = []
    for t in tot:
        if t not in d:
            ans.append([t, 10])
    #ans = []
    for k in d:
        print(k, d[k][-1])
        ans.append([k, d[k][-1]])
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["product_id"] = one
    res["price"] = two
    return res
    
    
