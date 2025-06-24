#1596
#medium

#Write a solution to find the most frequently ordered product(s) for each customer.

#The result table should have the product_id and product_name for each customer_id who ordered at least one order.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#map each value to the other

import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(orders["customer_id"]):
        d[v].append(orders["product_id"][i])
    print(d)
    fd = defaultdict(int)
    for k in d:
        biggest = -1
        for a in d[k]:
            biggest = max(biggest, d[k].count(a))
        fd[k] = biggest
    print(fd)
    prod = dict()
    for i, p in enumerate(products["product_id"]):
        prod[p] = products["product_name"][i]
    ansd = defaultdict(set)
    for f in fd:
        for a in d[f]:
            if d[f].count(a) == fd[f]:
                ansd[f].add(a)
    print(ansd)
    res = []
    for a in ansd:
        for k in ansd[a]:
            res.append([a, k, prod[k]])
    print(res)
    one, two, three = [], [], []
    for r in res:
        one.append(r[0])
        two.append(r[1])
        three.append(r[2])
    final = pd.DataFrame()
    final["customer_id"] = one
    final["product_id"] = two
    final["product_name"] = three

    return final
