#602
#medium

#Write a solution to find the people who have the most friends and the most friends number.

#The test cases are generated so that only one person has the most friends.

#The result format is in the following example.

#my own solution using python3:

#get the size of each list both ways 

import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    biggest = -1
    dd = defaultdict(list)
    for i, r in enumerate(request_accepted["accept_date"]):
        d[request_accepted["accepter_id"][i]] += 1
        dd[request_accepted["requester_id"][i]].append(request_accepted["accepter_id"][i])
        dd[request_accepted["accepter_id"][i]].append(request_accepted["requester_id"][i])

    print(dd)
    for k in dd:
        biggest = max(biggest, len(dd[k]))
    one, two = [], []
    for k in dd:
        if len(dd[k]) == biggest:
            one.append(k)
            two.append(len(dd[k]))
    res = pd.DataFrame()
    res["id"] = one
    res["num"] = two
    return res
