#3626
#medium


#Write a solution to find stores that have inventory imbalance - stores where the most expensive product has lower stock than the cheapest product.

#For each store, identify the most expensive product (highest price) and its quantity
#For each store, identify the cheapest product (lowest price) and its quantity
#A store has inventory imbalance if the most expensive product's quantity is less than the cheapest product's quantity
#Calculate the imbalance ratio as (cheapest_quantity / most_expensive_quantity)
#Round the imbalance ratio to 2 decimal places
#Only include stores that have at least 3 different products
#Return the result table ordered by imbalance ratio in descending order, then by store name in ascending order.

#The result format is in the following example.


#my own solution using python3:

#gather all the information piece by piece

import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    q = dict()
    name = dict()
    pn = dict()
    for i, s in enumerate(stores["store_id"]):
        name[s] = [stores["store_name"][i], stores["location"][i]]
    for i, s in enumerate(inventory["store_id"]):
        q[(s, inventory["price"][i])] = inventory["quantity"][i]
        pn[(s, inventory["price"][i])] = inventory["product_name"][i]
        d[s].append(inventory["price"][i])
        d[s].sort()
    ans = []
    for k in d:
        if len(d[k]) >= 3:
            cheap, exp = d[k][0], d[k][-1]
            if q[(k, exp)] < q[(k, cheap)]:
                ir = round(q[(k, cheap)] / q[(k, exp)], 2)
                ans.append([ir, k, name[k][0], name[k][1], pn[(k, exp)], pn[(k, cheap)]])
    ans.sort(key=lambda x: (-x[0], x[1]))
    print(ans)
    o, t, th, f, fi, ss = [], [], [], [], [], []
    for a in ans:
        o.append(a[1])
        t.append(a[2])
        th.append(a[3])
        f.append(a[4])
        fi.append(a[5])
        ss.append(a[0])
    res = pd.DataFrame()
    res["store_id"] = o
    res["store_name"] = t
    res["location"] = th
    res["most_exp_product"] = f
    res["cheapest_product"] = fi
    res["imbalance_ratio"] = ss
    return res

