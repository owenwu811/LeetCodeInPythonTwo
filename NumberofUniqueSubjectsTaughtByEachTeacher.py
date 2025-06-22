

#2356
#easy

#Write a solution to calculate the number of unique subjects each teacher teaches in the university.

#Return the result table in any order.

#The result format is shown in the following example.

#my own solution using python3:

#just follow the instructions

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(set)
    for i, t in enumerate(teacher["teacher_id"]):
        d[t].add(teacher["subject_id"][i])
    first, second = [], []
    for k in d:
        print(k, len(d[k]))
        first.append(k)
        second.append(len(d[k]))
    res = pd.DataFrame()
    res["teacher_id"] = first
    res["cnt"] = second
    return res
        
