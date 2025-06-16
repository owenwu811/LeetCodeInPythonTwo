#2084
#medium

#Write a solution to report all the orders based on the following criteria:

#If a customer has at least one order of type 0, do not report any order of type 1 from that customer.
#Otherwise, report all the orders of the customer.
#Return the result table in any order.


#my own solution using python3:

#just look at the examples and try to follow it

import pandas as pd

def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(orders["customer_id"]):
        d[v].append(orders["order_type"][i])
    #print(d)
    otoc = defaultdict(list)
    for i, v in enumerate(orders["order_id"]):
        if 0 in d[orders["customer_id"][i]]:
            if orders["order_type"][i] == 0:
                otoc[orders["order_id"][i]].append([orders["customer_id"][i], orders["order_type"][i]])
        else:
            otoc[orders["order_id"][i]].append([orders["customer_id"][i], orders["order_type"][i]])
    a = list(otoc.items())
    print(a)
    cnt = 0
    for b, c in a:
        print(b, c[0][0], c[0][1])
        orders["order_id"][cnt] = b
        orders["customer_id"][cnt] = c[0][0]
        orders["order_type"][cnt] = c[0][1]
        cnt += 1


    


    return pd.DataFrame(orders, columns=["order_id", "customer_id", "order_type"]).head(len(otoc))
