#2292
#medium

#Write a solution to report the IDs of all the products that were ordered three or more times in two consecutive years.

#Return the result table in any order.

#The result format is shown in the following example.


#my own solution using python3:

#get all the product ids for each purchase date, and then do a sliding window of size 2 over all the years and see the frequency of each common element for each of the two windows

import pandas as pd

def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, o in enumerate(orders["purchase_date"]):
        cur = str(o)[:4]
        d[cur].append(orders["product_id"][i])
    years = sorted(list(d.keys()))
    ans = []
    for i in range(1, len(years)):
        before, now = years[i - 1], years[i]
        #print(before, now)
        bb = d[before]
        nn = d[now]
        print(bb, nn)
        for num in bb:
            if num in nn:
                if bb.count(num) >= 3 and nn.count(num) >= 3:
                    if num not in ans:
                        ans.append(num)
    res = pd.DataFrame()
    res["product_id"] = ans
    return res

    #for k in d:
    #    print(k, d[k])
