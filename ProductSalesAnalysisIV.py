
#2324
#medium

#Write a solution that reports for each user the product id on which the user spent the most money. In case the same user spent the most money on two or more products, report all of them.

#Return the resulting table in any order.

#The result format is in the following example.



#my own solution using python3:

#use the key as the user id and the product id since we have to track the biggest price paid that way

import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    pr = dict()
    now = []
    for i, p in enumerate(product["product_id"]):
        pr[p] = product["price"][i]
    for i, s in enumerate(sales["product_id"]):
        #d[sales["user_id"][i]].append([s, (pr[s] * sales["quantity"][i])])
        d[(sales["user_id"][i], s)] += (pr[s] * sales["quantity"][i])
    #print(d)
    biggest = defaultdict(int)
    for k in d:
        biggest[k[0]] = max(biggest[k[0]], d[k])
    #print(biggest)
    one, two = [], []
    for k in d:
        if biggest[k[0]] == d[k]:
            print(k[0], k[1])
            one.append(k[0])
            two.append(k[1])
    res = pd.DataFrame()
    res["user_id"] = one
    res["product_id"] = two
    return res
    
