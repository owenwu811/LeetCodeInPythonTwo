
#3451
#Hard

#Write a solution to find invalid IP addresses. An IPv4 address is invalid if it meets any of these conditions:

#Contains numbers greater than 255 in any octet
#Has leading zeros in any octet (like 01.02.03.04)
#Has less or more than 4 octets
#Return the result table ordered by invalid_count, ip in descending order respectively. 

#The result format is in the following example.

#my own solution using python3:

#follow the instructions carefully

import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, v in enumerate(logs["ip"]):
        flag = True
        now = v.split(".")
        for n in now:
            if int(n) > 255 or n.startswith("0"):
                flag = False
        if v.count(".") != 3:
            flag = False
        if not flag:
            d[v] += 1
    d = list(d.items())
    d.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(d)
    logs["invalid_count"] = logs["log_id"]
    cnt = 0
    for a in d:
        logs["ip"][cnt] = a[0]
        logs["invalid_count"][cnt] = a[1]
        cnt += 1



    return pd.DataFrame(logs, columns=["ip", "invalid_count"]).head(len(d))
        
