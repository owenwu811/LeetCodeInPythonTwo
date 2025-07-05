#1204
#medium

#There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

#Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

#Note that only one person can board the bus at any given turn.

#The result format is in the following example.

#my own solution using python3:

#sort by the turns, and then keep adding until you can't

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, q in enumerate(queue["weight"]):
        cur.append([queue["turn"][i], q, queue["person_name"][i]])
    cur.sort(key=lambda x: x[0])
    print(cur)
    now = 0
    ans = []
    for c in cur:
        if now + c[1] <= 1000:
            now += c[1]
            print(c[-1])
            ans.append(c[-1])
        else:
            break
    ans = ans[-1:]
    res = pd.DataFrame()
    res["person_name"] = ans
    return res
       
