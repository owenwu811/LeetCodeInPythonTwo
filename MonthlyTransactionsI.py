#1193
#medium

#Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

#Return the result table in any order.

#The query result format is in the following example.

#my own solution using python3:

#use the date and country as the key to each dictionary, and then just extract the information needed as in the example

import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    tot = defaultdict(int)
    tamt = defaultdict(int)
    aprvtot = defaultdict(int)
    aprvcnt = defaultdict(int)
    for i, t in enumerate(transactions["country"]):
        dat = str(transactions["trans_date"][i]).split(" ")[0][:7]
        count = t
        tot[(t, dat)] += 1
        tamt[(t, dat)] += transactions["amount"][i]
        if transactions["state"][i] == "approved":
            aprvtot[(t, dat)] += transactions["amount"][i]
            aprvcnt[(t, dat)] += 1
    print(tot)
    print(tamt)
    print(aprvtot)
    one, two, three, four, five, six = [], [], [], [], [], []
    for t in tot:
        one.append(t[1])
        two.append(t[0])
        three.append(tot[t])
        four.append(aprvcnt[t])
        five.append(tamt[t])
        six.append(aprvtot[t])
    res = pd.DataFrame()
    res["month"] = one
    res["country"] = two
    res["trans_count"] = three
    res["approved_count"] = four
    res["trans_total_amount"] = five
    res["approved_total_amount"] = six
    return res
