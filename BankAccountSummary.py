
#1555
#medium

#Leetcode Bank (LCB) helps its coders in making virtual payments. Our bank records all transactions in the table Transaction, we want to find out the current balance of all users and check whether they have breached their credit limit (If their current credit is less than 0).

#Write a solution to report.

#user_id,
#user_name,
#credit, current balance after performing transactions, and
#credit_limit_breached, check credit_limit ("Yes" or "No")
#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#use loops to get the information you need and then get the sum of each person and see if it's below zero

import pandas as pd

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    dd = dict()
    for i, u in enumerate(users["user_id"]):
        d[u] = [users["credit"][i]]
        dd[u] = users["user_name"][i]
    for i, t in enumerate(transactions["paid_by"]):
        d[t].append(-transactions["amount"][i])
        d[transactions["paid_to"][i]].append(transactions["amount"][i])
    ans = []

    for k in d:
        #print(k, d[k])
        tot = sum(d[k])
        print(k, tot)
        if tot < 0:
            ans.append([k, dd[k], tot, "Yes"])
        else:
            ans.append([k, dd[k], tot, "No"])
    res = pd.DataFrame()
    one, two, three, four = [], [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
        four.append(a[3])
    res["user_id"] = one
    res["user_name"] = two
    res["credit"] = three
    res["credit_limit_breached"] = four
    return res


