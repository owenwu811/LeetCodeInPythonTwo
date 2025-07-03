#2474
#Hard

#Write a solution to report the IDs of the customers with the total purchases strictly increasing yearly.

#The total purchases of a customer in one year is the sum of the prices of their orders in that year. If for some year the customer did not make any order, we consider the total purchases 0.
#The first year to consider for each customer is the year of their first order.
#The last year to consider for each customer is the year of their last order.
#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#segregate each order date, and then fill in the years that are not there, and sort each value of each key in each dictionary

import pandas as pd

def find_specific_customers(orders: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, o in enumerate(orders["customer_id"]):
        now = str(orders["order_date"][i])[:4]
        d[(o, now)] += orders["price"][i]
    dd = defaultdict(list)
    for k in d:
        dd[k[0]].append([k[1], d[k]])
        dd[k[0]].sort()
    print(dd)
    ans = []
    for k in dd:
        flag = True
        small = int(dd[k][0][0])
        large = int(dd[k][-1][0])
        print(small, large)
        first = list(range(small, large + 1))
        for f in first:
            #print(f)
            flag = False
            for a in dd[k]:
                if int(a[0]) == f:
                    flag = True
                    break
            if not flag:
                print(f)
                dd[k].append([str(f), 0])
                dd[k].sort()

        for j in range(1, len(dd[k])):
            if dd[k][j][1] <= dd[k][j - 1][1]:
                flag = False
                break
        if flag:
            print(k)
            ans.append(k)
    res = pd.DataFrame()
    res["customer_id"] = ans
    return res
