#2238
#medium

#Write a solution to report the ID of each driver and the number of times they were a passenger.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#just loop through each column and count frequency in a dictionary

import pandas as pd

def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, v in enumerate(rides["driver_id"]):
        d[v] = 0
    for i, v in enumerate(rides["passenger_id"]):
        if v in d:
            d[v] += 1
    print(d)
    d = list(d.items())
    one, two = [], []
    for a in d:
        one.append(a[0])
        two.append(a[1])

    res = pd.DataFrame()
    res["driver_id"] = one
    res["cnt"] = two
    return res 
