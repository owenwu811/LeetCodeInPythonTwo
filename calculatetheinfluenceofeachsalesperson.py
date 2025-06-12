#2372
#medium

#Write a solution to report the sum of prices paid by the customers of each salesperson. If a salesperson does not have any customers, the total value should be 0.

#Return the result table in any order.

#The result format is shown in the following example.


#my own solution using python3:

#try to group each salespersonid to each customerid in the customer table, and use a dictionary to calculate the total amount of money they made

import pandas as pd

def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    ss = len(salesperson["salesperson_id"])
    d = defaultdict(int)
    for i, a in enumerate(customer["salesperson_id"]):
        cust = customer["customer_id"][i]
        if cust not in d:
            d[cust] = 0
        for j, v in enumerate(sales["customer_id"]):
            if v == cust:
                d[a] += sales["price"][j]
    print(d)
    sales["salesperson_id"] = salesperson["salesperson_id"]
    sales["name"] = salesperson["name"]
    sales["total"] = salesperson["salesperson_id"]
    for i, a in enumerate(sales["salesperson_id"]):
        sales["total"][i] = d[a]
    return pd.DataFrame(sales, columns=["salesperson_id", "name", "total"]).head(ss)
