#580
#medium

#Write a solution to report the respective department name and number of students majoring in each department for all departments in the Department table (even ones with no current students).

#Return the result table ordered by student_number in descending order. In case of a tie, order them by dept_name alphabetically.

#The result format is in the following example.


#my own solution using python3:

#use two dictionaries

import pandas as pd

def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, s in enumerate(student["dept_id"]):
        d[s] += 1
    idton = dict()
    for i, v in enumerate(department["dept_id"]):
        idton[v] = department["dept_name"][i]
    one, two = [], []
    ans = []
    for a, b in idton.items():
        print(b, d[a])
        ans.append([b, d[a]])
    ans.sort(key=lambda x: x[1], reverse=True)
    for a in ans:
        one.append(a[0])
        two.append(a[1])

    res = pd.DataFrame()
    res["dept_name"] = one
    res["student_number"] = two
    return res
