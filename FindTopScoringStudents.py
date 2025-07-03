
#3182
#medium

#Write a solution to find the students who have taken all courses offered in their major and have achieved a grade of A in all these courses.

#Return the result table ordered by student_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#map the studentid to major, and then get all the major requirements, and then see what each student enrolled, and compare the two lists

import pandas as pd

def find_top_scoring_students(enrollments: pd.DataFrame, students: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:
    req = dict()
    for i, s in enumerate(students["name"]):
        req[students["student_id"][i]] = students["major"][i]
    maj = defaultdict(list)
    for i, c in enumerate(courses["major"]):
        maj[c].append(courses["course_id"][i])
    print(maj)
    print(req)
    done = defaultdict(list)
    for i, e in enumerate(enrollments["grade"]):
        if e == "A":
            done[enrollments["student_id"][i]].append(enrollments["course_id"][i])
    print(done)
    ans = []
    for d in done:
        majj = req[d]
        #print(majj)
        reqq = maj[majj]
        #print(reqq, done[d])
        if Counter(done[d]) >= Counter(reqq):
            print(d)
            ans.append(d)
    res = pd.DataFrame()
    res["student_id"] = ans
    return res
