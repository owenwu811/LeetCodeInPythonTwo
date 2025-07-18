#2112
#medium

#Write a solution to report the ID of the airport with the most traffic. The airport with the most traffic is the airport that has the largest total number of flights that either departed from or arrived at the airport. If there is more than one airport with the most traffic, report them all.

#Return the result table in any order.

#The result format is in the following example.



#my own solution using python3:

#just tally up the frequencies of both depart and arrive columns and find the biggest frequency

import pandas as pd

def airport_with_most_traffic(flights: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, f in enumerate(flights["departure_airport"]):
        d[f] += flights["flights_count"][i]
        d[flights["arrival_airport"][i]] += flights["flights_count"][i]
    biggest = 0
    for k in d:
        print(k, d[k])
        biggest = max(biggest, d[k])
    ans = []
    for k in d:
        if d[k] == biggest:
            ans.append(k)
    res = pd.DataFrame()
    res["airport_id"] = ans
    return res


