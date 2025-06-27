
#1077
#medium

#Write a solution to report the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#gather all project ids and their employee ids, and then loop over each project id, each employee id, and find the biggest experience

import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, p in enumerate(project["project_id"]):
        d[p].append(project["employee_id"][i])
    ans = []
    for k in d:
        cur = []
        biggest = -1
        for a in d[k]:
            for i, e in enumerate(employee["employee_id"]):
                if a == e:
                    biggest = max(biggest, employee["experience_years"][i])
                    cur.append([e, employee["experience_years"][i]])
        print(k, cur, biggest)
        for c in cur:
            if c[1] == biggest:
                print(k, c[0])
                ans.append([k, c[0]])
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["project_id"] = one
    res["employee_id"] = two
    return res
