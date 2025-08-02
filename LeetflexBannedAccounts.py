#1747
#medium

#Write a solution to find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#get the account ids as the keys, and then append the start and end and ip address, and then try to find an intersection with different ip to include that key in res list

import pandas as pd

def leetflex_banned_accnts(log_info: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, l in enumerate(log_info["account_id"]):
        login, logout = log_info["login"][i], log_info["logout"][i]
        d[l].append([login, logout, log_info["ip_address"][i]])
        d[l].sort(key=lambda x: (x[0], x[1]))
    ans = []
    for k in d:
        print(k, d[k])
        for j in range(len(d[k])):
            
            s, e, val = d[k][j][0], d[k][j][1], d[k][j][-1]
            for a in range(len(d[k])):
                if a != j:
                    ss, ee, cval = d[k][a][0], d[k][a][1], d[k][a][-1]
                    if ss <= e and ee > s or ee >= s and e > ss:
                        if cval != val:
                            print(k)
                            if k not in ans: ans.append(k)
    res = pd.DataFrame()
    res["account_id"] = ans
    return res
