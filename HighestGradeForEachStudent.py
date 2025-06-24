
#1112
#medium

#Write a solution to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.

#Return the result table ordered by student_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#get the student ids, and use two dictionaries to get the lowest of one value and highest of another

import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, e in enumerate(enrollments["student_id"]):
        d[e].append(enrollments["grade"][i])
        d[e].sort()
    print(d)
    c = defaultdict(list)
    for i, e in enumerate(enrollments["student_id"]):
        if enrollments["grade"][i] == d[e][-1]:
            c[e].append(enrollments["course_id"][i])
            c[e].sort()
    ans = []
    for k in d:
        one, two, three = k, c[k][0], d[k][-1]
        ans.append([one, two, three])
    ans.sort()
    print(ans)
    a, b, c = [], [], []
    for y in ans:
        a.append(y[0])
        b.append(y[1])
        c.append(y[2])
    res = pd.DataFrame()
    res["student_id"] = a
    res["course_id"] = b
    res["grade"] = c
    return res
