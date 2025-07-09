#626
#medium

#Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

#Return the result table ordered by id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#use a hashmap, and swap using another array to keep track of ids

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    vals = []
    for i, s in enumerate(seat["id"]):
        d[s] = seat["student"][i]
        vals.append(s)
    for i in range(1, len(vals), 2):
        prev, cur = vals[i - 1], vals[i]
        print(prev, cur)
        bp, bc = d[prev], d[cur]
        print(bp, bc)
        d[cur], d[prev] = bp, bc
    print(d)
    one, two = [], []
    for k in d:
        one.append(k)
        two.append(d[k])
    res = pd.DataFrame()
    res["id"] = one
    res["student"] = two
    return res
