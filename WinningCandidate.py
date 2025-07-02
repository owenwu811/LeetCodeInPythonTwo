
#574
#medium

#Write a solution to report the name of the winning candidate (i.e., the candidate who got the largest number of votes).

#The test cases are generated so that exactly one candidate wins the elections.

#The result format is in the following example.

#my own solution using python3:

#map name to id, and then tally up id votes, find the maximum, and map back to original dict

import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    for i, c in enumerate(candidate["name"]):
        d[candidate["id"][i]] = c
    dd = defaultdict(int)
    for i, v in enumerate(vote["candidateId"]):
        dd[v] += 1
    print(dd)
    ans = []
    target = max(dd.values())
    for a, b in dd.items():
        if b == target:
            print(d[a])
            ans.append(d[a])
    res = pd.DataFrame()
    res["name"] = ans
    return res
