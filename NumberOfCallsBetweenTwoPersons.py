
#1699
#medium

#Write a solution to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

#Return the result table in any order.

#The result format is in the following example


#my own solution using python3:

#just follow the directions

import pandas as pd

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    cnt = defaultdict(int)
    for i, v in enumerate(calls["from_id"]):
        f, t = v, calls["to_id"][i]
        now = []
        now.append(f)
        now.append(t)
        now.sort()
        d[tuple(now)] += calls["duration"][i]
        cnt[tuple(now)] += 1
    #print(d)
    #print(cnt)
    one = list(d.items())
    two = list(cnt.items())
    print(one, two)
    calls["person1"] = calls["from_id"]
    calls["person2"] = calls["from_id"]
    calls["call_count"] = calls["from_id"]
    calls["total_duration"] = calls["from_id"]
    i = 0
    for j in range(len(calls["person1"])):
        if i < len(one) and i < len(two):
            print(one[i])
            calls["person1"][i] = one[i][0][0]
            calls["person2"][i] = one[i][0][1]
            calls["call_count"][i] = two[i][-1]
            calls["total_duration"][i] = one[i][-1]
            i += 1


    return pd.DataFrame(calls, columns=["person1", "person2", "call_count", "total_duration"]).head(len(d))
