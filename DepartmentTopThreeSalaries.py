#185
#hard

#A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

#Write a solution to find the employees who are high earners in each of the departments.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#loop over each table to get the info you need

import pandas as pd


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    dpt = dict()
    for i, v in enumerate(department["id"]):
        dpt[v] = department["name"][i]
    ss = defaultdict(list)
    for i, e in enumerate(employee["salary"]):
        d[employee["departmentId"][i]].append(e)
        if e not in ss[employee["departmentId"][i]]:
            ss[employee["departmentId"][i]].append(e)
            ss[employee["departmentId"][i]].sort()
        d[employee["departmentId"][i]].sort()
    ans = []
    for k in ss:
        if len(ss[k]) >= 3:
            for i, e in enumerate(employee["salary"]):
                if e in ss[k][-3:] and employee["departmentId"][i] == k:
                    print(employee["departmentId"][i], employee["name"][i], employee["salary"][i])
                    one, two, three = dpt[employee["departmentId"][i]], employee["name"][i], employee["salary"][i]
                    ans.append([one, two, three])
        else:
            #print(k, ss[k])
            for i, e in enumerate(employee["salary"]):
                if e in ss[k] and employee["departmentId"][i] == k:
                    one, two, three = dpt[employee["departmentId"][i]], employee["name"][i], employee["salary"][i]
                    ans.append([one, two, three])
    print(ans)
    a, b, c = [], [], []
    for u in ans:
        a.append(u[0])
        b.append(u[1])
        c.append(u[2])
    res = pd.DataFrame()
    res["Department"] = a
    res["Employee"] = b
    res["Salary"] = c

    return res
