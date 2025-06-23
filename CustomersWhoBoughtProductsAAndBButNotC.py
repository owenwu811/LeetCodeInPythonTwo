#1398
#medium

#Write a solution to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them to purchase this product.

#Return the result table ordered by customer_id.

#The result format is in the following example.


#my own solution using python3:

#very easy - just do exactly what is asked

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, o in enumerate(orders["customer_id"]):
        d[o].append(orders["product_name"][i])
    ppl = dict()
    for i, c in enumerate(customers["customer_id"]):
        ppl[c] = customers["customer_name"][i]
    ans = []
    for k in d:
        if "C" not in d[k] and "A" in d[k] and "B" in d[k]:
            print(k, ppl[k])
            ans.append([k, ppl[k]])
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["customer_id"] = one
    res["customer_name"] = two
    return res
