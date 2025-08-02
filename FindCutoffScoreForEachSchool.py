#1988
#medium

#Every year, each school announces a minimum score requirement that a student needs to apply to it. The school chooses the minimum score requirement based on the exam results of all the students:

#They want to ensure that even if every student meeting the requirement applies, the school can accept everyone.
#They also want to maximize the possible number of students that can apply.
#They must use a score that is in the Exam table.
#Write a solution to report the minimum score requirement for each school. If there are multiple score values satisfying the above conditions, choose the smallest one. If the input data is not enough to determine the score, report -1.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#loop through all school ids, and then check all the exam's students counts against the capacity, and then find the smallest capit exam score for that condition

import pandas as pd

def find_cutoff_score(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    for i, s in enumerate(schools["school_id"]):
        cap = schools["capacity"][i]
        cur = []
        for j, e in enumerate(exam["student_count"]):
            if e <= cap:
                cur.append(exam["score"][j])
                cur.sort()
        print(s, cur)
        if not cur:
            d[s] = -1
        else: 
            d[s] = cur[0]
        print(s, cur)
    print(d)
    one, two = [], []
    ans = []
    for a, b in d.items():
        ans.append([a, b])
        #one.append(a)
        #two.append(b)
    ans.sort(key=lambda x: (-x[1]))
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["school_id"] = one
    res["score"] = two

    return res
