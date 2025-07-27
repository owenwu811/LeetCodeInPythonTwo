#1303
#easy

#Write a solution to find the team size of each of the employees.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#use a dictionary to map the team ids to their frequencies

import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    c = Counter(employee["team_id"])
    print(c)
    d = defaultdict(int)
    for i, e in enumerate(employee["employee_id"]):
        d[e] = c[employee["team_id"][i]]
    print(d)
    ans = []
    one, two = [], []
    for a, b in d.items():
        one.append(a)
        two.append(b)
    res = pd.DataFrame()
    res["employee_id"] = one
    res["team_size"] = two
    return res
    
