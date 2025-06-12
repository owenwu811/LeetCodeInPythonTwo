
#1445
#medium

#Write a solution to report the difference between the number of apples and oranges sold each day.

#Return the result table ordered by sale_date.

#The result format is in the following example.


#my own solution using python3:

#follow the instructions exactly

import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    seen = []
    d = defaultdict(list)
    for i, a in enumerate(sales["sale_date"]):
        a = str(a).split(" ")
        if a[0] not in seen:
            heapq.heappush(seen, a[0])
      
        d[a[0]].append(sales["sold_num"][i])
        #seen.add(a)
    #print(seen)
    print(d)
    cnt = 0
    sales["diff"] = sales["sold_num"]
    for k in d:
        sales["sale_date"][cnt] = k
        cur = d[k][0]
        for j in range(1, len(d[k])):
            cur -= d[k][j]
        print(cur)
        sales["diff"][cnt] = cur
        cnt += 1

    
    return pd.DataFrame(sales, columns=["sale_date", "diff"]).head(len(seen))
