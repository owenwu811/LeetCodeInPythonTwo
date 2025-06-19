#1412
#Hard

#A quiet student is the one who took at least one exam and did not score the highest or the lowest score.

#Write a solution to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.

#Return the result table ordered by student_id.

#The result format is in the following example.

#my own solution using python3:

#try to rule out all students that ever have the biggest or smallest score for that particular exam id first

import pandas as pd

def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, e in enumerate(exam["exam_id"]):
        d[e].append(exam["score"][i])
        d[e].sort()
    print(d)
    od = dict()
    seen = set()
    for i, s in enumerate(exam["student_id"]):
        seen.add(s)
        cur = d[exam["exam_id"][i]]
        if exam["score"][i] == cur[0] or exam["score"][i] == cur[-1]:
            od[s] = False
    print(od)
    new = seen.difference(set(od.keys()))
    print(new)
    ansd = dict()
    for i, s in enumerate(student["student_id"]):
        if s in new:
            ansd[s] = student["student_name"][i]
    print(ansd)
    ansd = list(ansd.items())
    cnt = 0
    for i, s in enumerate(student["student_id"]):
        if cnt < len(ansd):
            student["student_id"][cnt] = ansd[cnt][0]
            student["student_name"][cnt] = ansd[cnt][1]
            cnt += 1

    return pd.DataFrame(student, columns=["student_id", "student_name"]).head(len(ansd))
