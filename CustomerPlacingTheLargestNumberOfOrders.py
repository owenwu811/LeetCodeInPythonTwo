#586
#easy

#Write a solution to find the customer_number for the customer who has placed the largest number of orders.

#The test cases are generated so that exactly one customer will have placed more orders than any other customer.

#The result format is in the following example.

#my own solution using python3:

#tally up with a hashmap, and then get the largest one - note the edge case with empty data

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, o in enumerate(orders["customer_number"]):
        d[o] += 1
    ans = []
    if d:
        biggest = max(d.values())
        for a, b in d.items():
            if b == biggest:
                ans.append(a)
        res = pd.DataFrame()
        res["customer_number"] = ans
        return res
    return pd.DataFrame(columns=["customer_number"])
