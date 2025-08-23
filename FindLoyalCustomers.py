#3657
#medium

#Write a solution to find loyal customers. A customer is considered loyal if they meet ALL the following criteria:

#Made at least 3 purchase transactions.
#Have been active for at least 30 days.
#Their refund rate is less than 20% .
#Return the result table ordered by customer_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#follow the instructions exactly as asked

import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    dat = defaultdict(list)
    pc = defaultdict(int)
    rr = defaultdict(list)
    for i, c in enumerate(customer_transactions["customer_id"]):
        if customer_transactions["transaction_type"][i] == "purchase":
            pc[c] += 1
        rr[c].append(customer_transactions["transaction_type"][i])
        dat[c].append(customer_transactions["transaction_date"][i])
        dat[c].sort()
    ans = []
    for k in dat:
        ratio = rr[k].count('refund') / len(rr[k])
        period = str(pd.to_datetime(dat[k][-1]) - pd.to_datetime(dat[k][0])).split(" ")[0]

        #print(period)
        if ratio < 0.2 or 'refund' not in rr[k]:
            if int(period) >= 30 and len(rr[k]) >= 3:
                print(k, rr[k], dat[k])
                ans.append(k)
    res = pd.DataFrame()
    res["customer_id"] = ans
    return res
        
    
    
