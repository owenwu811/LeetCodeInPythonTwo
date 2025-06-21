
#2988
#medium

#Write a solution to find the name of the manager from the largest department. There may be multiple largest departments when the number of employees in those departments is the same.

#Return the result table sorted by dep_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#just follow the instructions exactly

import pandas as pd

def find_manager(employees: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    biggest = 0
    for i, v in enumerate(employees["dep_id"]):
        d[v] += 1
        biggest = max(biggest, d[v])
    print(d)
    ans = []
    for k in d:
        if d[k] == biggest:
            ans.append(k)
    #print(ans)
    res = []
    for a in ans:
        for i, v in enumerate(employees["dep_id"]):
            if v == a:
                if employees["position"][i] == "Manager":
                    #print(employees["emp_name"][i], v)
                    res.append([employees["emp_name"][i], v])
    res.sort(key=lambda x: x[1])
    print(res)
    employees["manager_name"] = employees["emp_name"]
    cnt = 0
    for r in res:
        employees["manager_name"][cnt] = r[0]
        employees["dep_id"][cnt] = r[1]
        cnt += 1
    return pd.DataFrame(employees, columns=["manager_name", "dep_id"]).head(len(res))
