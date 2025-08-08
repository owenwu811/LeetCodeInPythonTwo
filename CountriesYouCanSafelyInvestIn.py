#1501
#medium

#my own solution using python3:

#use hashmaps to gather the results and to map the foreign key column from one table to another

import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    a = sum(calls["duration"])
    glob = a / len(calls["duration"])
    d = defaultdict(list)
    mapp = dict()
    for i, c in enumerate(country["name"]):
        mapp[country["country_code"][i]] = c
    for i, p in enumerate(person["phone_number"]):
        first = p[:3]
        if first in mapp:
            #print(mapp[first])
            d[mapp[first]].append(person["id"][i])
    #print(d)
    tot = defaultdict(list)
    for i, c in enumerate(calls["caller_id"]):
        for k in d:
            for a in d[k]:
                if c == a:
                    tot[k].append(calls["duration"][i])
        for k in d:
            for a in d[k]:
                if calls["callee_id"][i] == a:
                    tot[k].append(calls["duration"][i])
    #print(tot)
    #print(glob)
    ans = []
    for t in tot:
        print(t, tot[t])
        cur = sum(tot[t]) // len(tot[t])
        print(cur)
        if cur > glob:
            print(t)
            ans.append(t)
    res = pd.DataFrame()
    res["country"] = ans
    return res

            
