#2362
#Hard

#Write a solution to show the details of the invoice with the highest price. If two or more invoices have the same price, return the details of the one with the smallest invoice_id.

#Return the result table in any order.

#The result format is shown in the following example.


#my own solution using python3:

#use the invoice ids to calculate the maximum cost

import pandas as pd

def generate_the_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    pr = dict()
    for i, p in enumerate(products["product_id"]):
        pr[p] = products["price"][i]
    d = defaultdict(int)
    for i, p in enumerate(purchases["invoice_id"]):
        q = purchases["quantity"][i]
        cost = pr[purchases["product_id"][i]] * q
        print(purchases["invoice_id"][i], cost)
        d[purchases["invoice_id"][i]] += cost
    biggest = -1
    for k in d:
        biggest = max(biggest, d[k])
    print(biggest)
    ans = []
    for k in d:
        if d[k] == biggest:
            ans.append(k)
    ans.sort()
    print(ans)
    first, second, third = [], [], []
    for i, p in enumerate(purchases["invoice_id"]):
        if p == ans[0]:
            one, two, three = purchases["product_id"][i], purchases["quantity"][i], purchases["quantity"][i] * pr[purchases["product_id"][i]]
            print(one, two, three)
            first.append(one)
            second.append(two)
            third.append(three)
    res = pd.DataFrame()
    res["product_id"] = first
    res["quantity"] = second
    res["price"] = third
    return res
