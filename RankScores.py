#178
#medium

#Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

#The scores should be ranked from the highest to the lowest.
#If there is a tie between two scores, both should have the same ranking.
#After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
#Return the result table ordered by score in descending order.

#The result format is in the following example.



#my own solution using python3:

#just sort the scores in descending order and account for duplicates

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, s in enumerate(scores["score"]):
        cur.append(s)
    cur.sort(reverse=True)
    print(cur)
    ans = []
    cnt = 1
    for i, c in enumerate(cur):
        if i >= 1:
            if cur[i] != cur[i - 1]:
                cnt += 1
        print(c, cnt)
        ans.append([c, cnt])
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["score"] = one
    res["rank"] = two
    return res
