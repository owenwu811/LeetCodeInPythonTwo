#1350
#easy

#Find the id and the name of all students who are enrolled in departments that no longer exist.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#follow the instructions

import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    exist = set()
    c = 0
    for i, v in enumerate(departments["id"]):
        exist.add(v)
    for i, s in enumerate(students["department_id"]):
        if s not in exist:
            c += 1
    print(c)
    departments["id"] = students["id"]
    departments["name"] = students["name"]
    a = pd.DataFrame()
    a["id"] = students["id"]
    a["name"] = students["name"]
    #print(a)
    diff = len(departments["id"]) - len(exist)
    left = set()
    for i, s in enumerate(students["department_id"]):
        if s not in exist:
            left.add(s)
    print(left)
    #print(departments)
    cnt = 0
    for i, s in enumerate(students["department_id"]):
        if s in left:
            #print(s, students["id"][i], students["name"][i])
            a["id"][cnt] = students["id"][i]
            a["name"][cnt] = students["name"][i]
            cnt += 1

    return pd.DataFrame(a, columns=["id", "name"]).head(c)
