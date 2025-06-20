
#3293
#medium

#Write a solution to find the final price of each product after applying the category discount. If a product's category has no associated discount, its price remains unchanged.

#Return the result table ordered by product_id in ascending order.

#The result format is in the following example.


#my own solution using python3:

#just follow the directions

import pandas as pd

def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    for i, v in enumerate(discounts["category"]):
        d[v] = discounts["discount"][i]
    print(d)
    ans = []
    for i, v in enumerate(products["product_id"]):
        if products["category"][i] in d:
            final = products["price"][i] - ((d[products["category"][i]] / 100) * products["price"][i])
            #final = int(final)
            #print(v, final, products["category"][i])
            ans.append([v, final, products["category"][i]])
        else:
            #print(v, products["price"][i], products["category"][i])
            ans.append([v, products["price"][i], products["category"][i]])
    ans.sort()
    print(ans)
    products["final_price"] = products["price"]
    cnt = 0
    for a in ans:
        products["product_id"][cnt] = a[0]
        products["final_price"][cnt] = a[1]
        products["category"][cnt] = a[2]
        cnt += 1


    return pd.DataFrame(products, columns=["product_id", "final_price", "category"])
