#2880
#easy

#Write a solution to select the name and age of the student with student_id = 101.

#The result format is in the following example.

#my own solution using python3:

#just loop through and get the rows with sid = 101

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    ans = list()
    for i, s in enumerate(students["student_id"]):
        if s == 101:
            ans.append([students["name"][i], students["age"][i]])
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    
    res = pd.DataFrame()
    res["name"] = one
    res["age"] = two
    
    return res
