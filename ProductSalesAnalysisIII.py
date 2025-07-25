#1070
#medium

#Write a solution to find all sales that occurred in the first year each product was sold.

#For each product_id, identify the earliest year it appears in the Sales table.

#Return all sales entries for that product in that year.

#Return a table with the following columns: product_id, first_year, quantity, and price.
#Return the result in any order.

#my own solution using python3:

#find the 1st year for each product id, and record all the entries with that product id and 1st year

import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, s in enumerate(sales["product_id"]):
        d[s].append([sales["year"][i], sales["quantity"][i], sales["price"][i]])
        d[s].sort(key=lambda x: (x[0]))
    ans = []
    for k in d:
        print(k, d[k])
        y = d[k][0][0]
        for a in d[k]:
            if a[0] == y:
                ans.append([k, a[0], a[1], a[2]])
    one, two, three, four = [], [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
        four.append(a[3])
    res = pd.DataFrame()
    res["product_id"] = one
    res["first_year"] = two
    res["quantity"] = three
    res["price"] = four
    return res
