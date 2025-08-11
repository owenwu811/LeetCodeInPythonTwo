#1174
#medium

#If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

#The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

#Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

#The result format is in the following example.

#my own solution using python3:

#gather all first time orders before using the cust id and first time order date to evaluate if we even care about this row or not, and then calculate ratio without duplicates

import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    cust = defaultdict(list)
    for i, d in enumerate(delivery["customer_id"]):
        cust[d].append(delivery["order_date"][i])
        cust[d].sort()
    print(cust)
    imm, sch = [], []
    for c in cust:
        #print(c, cust[c][0])
        for i, d in enumerate(delivery["customer_id"]):
            if d == c and delivery["order_date"][i] == cust[c][0]:
                if delivery["order_date"][i] == delivery["customer_pref_delivery_date"][i]:
                    if c not in imm: imm.append(c)
                else:
                    if c not in sch: sch.append(c)
    print(imm, sch)
    tot = len(imm) + len(sch)
    ans = (len(imm) / tot) * 100
    ans = round(ans, 2)
    print(ans)
    res = pd.DataFrame()
    res["immediate_percentage"] = [ans]
    return res
