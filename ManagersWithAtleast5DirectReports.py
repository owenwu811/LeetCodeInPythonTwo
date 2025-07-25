
#570
#medium

#Write a solution to find managers with at least five direct reports.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#map the id to name, and then if an employee is not who the manager is, record that in a dictionary value with the manager as the key, and then loop over the dictionary, and compare bigger than or equal to 5

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(set)
    employee.dropna()
    for i, e in enumerate(employee["managerId"]):
        try:
            if employee["id"][i] != e:
                d[e].add(employee["id"][i])
        except:
            continue
    m = defaultdict(str)
    for i, e in enumerate(employee["id"]):
        m[e] = employee["name"][i]
    ans = []
    for k in d:
        print(k, d[k])
        if len(d[k]) >= 5 and k in m:
            ans.append(m[k])
    res = pd.DataFrame()
    res["name"] = ans
    return res
