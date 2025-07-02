
#184
#medium

#Write a solution to find employees who have the highest salary in each of the departments.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#just loop through each time to get what you need

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    dd = dict()
    for i, e in enumerate(department["id"]):
        dd[e] = department["name"][i]
    for i, e in enumerate(employee["departmentId"]):
        d[e].append([employee["salary"][i], employee["name"][i], dd[e]])
        d[e].sort()
    bd = defaultdict(int)
    for k in d:
        #print(k, d[k])
        biggest = -1
        for a in d[k]:
            biggest = max(biggest, a[0])
        bd[k] = biggest
    one, two, three = [], [], []
    for k in d:
        for a in d[k]:
            if a[0] == bd[k]:
                print(a)
                one.append(a[0])
                two.append(a[1])
                three.append(a[2])
    res = pd.DataFrame()
    res["Department"] = one
    res["Employee"] = two
    res["Salary"] = three
    return res
