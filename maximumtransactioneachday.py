
#1831
#medium

#Write a solution to report the IDs of the transactions with the maximum amount on their respective day. If in one day there are multiple such transactions, return all of them.

#Return the result table ordered by transaction_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#messy but working


import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(transactions["day"]):
        cur = str(v).split(" ")
        #print(cur)
        d[cur[0]].append(transactions["amount"][i])
        d[cur[0]].sort()
    #print(d)

    ans = []
    for k in d:
        last = d[k][-1]
        for i, t in enumerate(transactions["transaction_id"]):
            v = str(transactions["day"][i]).split(" ")[0]
            #print(v)
            #print(d[v], t, transactions["amount"][i])
            if d[v][-1] == transactions["amount"][i]:
                #print(t)
                if t not in ans:
                    heapq.heappush(ans, t)
    ans.sort()
    print(ans)
    cnt = 0
    for i, v in enumerate(transactions["transaction_id"]):
        if cnt < len(ans):
            transactions["transaction_id"][i] = ans[cnt]
            cnt += 1
    return pd.DataFrame(transactions, columns=["transaction_id"]).head(len(ans))
