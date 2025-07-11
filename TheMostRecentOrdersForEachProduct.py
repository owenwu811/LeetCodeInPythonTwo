
#1549
#medium

#Write a solution to find the most recent order(s) of each product.

#Return the result table ordered by product_name in ascending order and in case of a tie by the product_id in ascending order. If there still a tie, order them by order_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#collect all the data you need, and sort it accordingly

import pandas as pd

def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    cur = []
    d = dict()
    for i, p in enumerate(products["product_id"]):
        d[p] = products["product_name"][i]
    for i, p in enumerate(orders["product_id"]):
        od = str(orders["order_date"][i]).split(" ")[0]
        cur.append([od, p, orders["order_id"][i], d[p]])
    cur.sort(key=lambda x: x[0])
    #print(cur)
    dd = defaultdict(list)
    for c in cur:
        dd[c[-1]].append(c[:-1])
        dd[c[-1]].sort()
    ans = []
    for k in dd:
       # print(k, dd[k])
        biggest = dd[k][-1][0]
        #print(biggest)
        for a in dd[k]:
            if a[0] == biggest:
                ans.append([k, a[1], a[2], biggest])
    ans.sort(key=lambda x: (x[0], x[1], x[2]))
    print(ans)
    o, t, th, f = [], [], [], []
    for a in ans:
        o.append(a[0])
        t.append(a[1])
        th.append(a[2])
        f.append(a[3])
    res = pd.DataFrame()
    res["product_name"] = o
    res["product_id"] = t
    res["order_id"] = th
    res["order_date"] = f
    return res


    #[['2020-06-10', 2, 5, 'mouse'], ['2020-07-15', 2, 10, 'mouse'], 
    #['2020-07-29', 1, 4, 'keyboard'], ['2020-07-30', 2, 2, 'mouse'], 
    #['2020-07-31', 1, 1, 'keyboard'], ['2020-08-01', 1, 6, 'keyboard'], 
    #['2020-08-01', 1, 7, 'keyboard'], ['2020-08-03', 2, 8, 'mouse'], 
    #['2020-08-07', 3, 9, 'screen'], ['2020-08-29', 3, 3, 'screen']]
