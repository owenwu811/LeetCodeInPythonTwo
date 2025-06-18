
#2994
#hard

#Write a solution to calculate the total spending by users on each Friday of every week in November 2023. If there are no purchases on a particular Friday of a week, it will be considered as 0.

#Return the result table ordered by week of month in ascending order.

#The result format is in the following example.


#my own solution using python3:

#messy but working solution

import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    cur = ["m", 't', 'w', 'th', 'f', 'sat', 'sun']
    for i in range(31):
        d[i - 1] = cur[i % len(cur)]
    #print(d)
    ansd = defaultdict(int)
    need = set()
    for k in d:
        if d[k] == "f":
            #print(k)
            for i, p in enumerate(purchases["purchase_date"]):
                cur = str(p).split(" ")
                now = cur[0][-2:]
                if int(now) == k:
                    ansd[cur[0]] += purchases["amount_spend"][i]
                elif d[k] == "f":
                    #print(cur[0])
                    flag = False
                    #print(k, ansd)
                    need.add(k)
                    
    print(ansd)
    print(need)
    for n in need:
        cur = str(n)
        #print(cur)
        flag = False
        for a in ansd:
            if a.endswith(cur):
                flag = True
                break
        if not flag:
            #print(cur)
            if 1 <= n <= 9:
                cur = "0" + cur

            ansd["2023-11-" + cur] = 0
    print(ansd)
    sl = []
    for a in ansd:
        sl.append((a, ansd[a]))
    sl.sort()
    print(sl)
    cur = 1
    purchases["week_of_month"] = purchases["user_id"]
    purchases["total_amount"] = purchases["user_id"]
    for i, s in enumerate(sl):
        purchases["week_of_month"][i] = cur
        purchases["purchase_date"][i] = s[0]
        purchases["total_amount"][i] = s[1]

        cur += 1
    


    return pd.DataFrame(purchases, columns=["week_of_month", "purchase_date", "total_amount"]).head(4)

            
                
