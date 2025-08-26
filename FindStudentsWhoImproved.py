#3421
#medium

#Write a solution to find the students who have shown improvement. A student is considered to have shown improvement if they meet both of these conditions:

#Have taken exams in the same subject on at least two different dates
#Their latest score in that subject is higher than their first score
#Return the result table ordered by student_id, subject in ascending order.

#The result format is in the following example.

#my own solution using python3:

#get the student id + the subject id as the key, and then use a list to get the exam date + scores, sorting that list by the exam date to compare

import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    dates = defaultdict(set)
    tot = defaultdict(list)
    for i, s in enumerate(scores["student_id"]):
        tot[(s, scores["subject"][i])].append([scores["exam_date"][i], scores["score"][i]])
        tot[(s, scores["subject"][i])].sort(key=lambda x: x[0])
        dates[(s, scores["subject"][i])].add(scores["exam_date"][i])
    second = dict()
    for k in dates:
        if len(dates[k]) >= 2:
            for a in dates[k]:
                second[(k[0], k[1], a)] = []
    ans = []
    for t in tot:
        now = tot[t]
        if now[0][1] < now[-1][1]:
            print(t, now[0][1], now[-1][1])
            ans.append([t[0], t[1], now[0][1], now[-1][1]])
    ans.sort(key=lambda x: (x[0], x[1]))
    print(ans)
    a, b, c, d = [], [], [], []
    for l in ans:
        a.append(l[0])
        b.append(l[1])
        c.append(l[2])
        d.append(l[3])
    res = pd.DataFrame()
    res["student_id"] = a
    res["subject"] = b
    res["first_score"] = c
    res["latest_score"] = d
    return res
