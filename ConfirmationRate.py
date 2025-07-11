
#1934
#medium

#The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

#Write a solution to find the confirmation rate of each user.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#use a dictionary to gather the ratios of timeouts and confirmations

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, s in enumerate(signups["user_id"]):
        for j, c in enumerate(confirmations["action"]):
            if confirmations["user_id"][j] == s:
                if c == "timeout":
                    d[s].append("t")
                else:
                    d[s].append("c")
        if s not in d:
            d[s].append("z")
    print(d)
    ans = []
    for k in d:
        if "t" not in d[k] and "c" in d[k]:
            ans.append([k, 1.00])
        elif "c" not in d[k]:
            ans.append([k, 0.00])
        elif "t" not in d[k] and "c" not in d[k]:
            ans.append([k, 0.00])
        else:
            val = round(d[k].count("c") / len(d[k]), 2)

            ans.append([k, val])
    print(ans)
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["user_id"] = one
    res["confirmation_rate"] = two
    return res

            
    
