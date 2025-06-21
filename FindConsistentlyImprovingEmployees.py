#3580
#medium

#Write a solution to find employees who have consistently improved their performance over their last three reviews.

#An employee must have at least 3 review to be considered
#The employee's last 3 reviews must show strictly increasing ratings (each review better than the previous)
#Use the most recent 3 reviews based on review_date for each employee
#Calculate the improvement score as the difference between the latest rating and the earliest rating among the last 3 reviews
#Return the result table ordered by improvement score in descending order, then by name in ascending order.

#The result format is in the following example.


#my own solution using python3:

#follow the instructions exactly

import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, e in enumerate(performance_reviews["employee_id"]):
        d[e].append([performance_reviews["review_date"][i], performance_reviews["rating"][i]])
        d[e].sort()
    emp = dict()
    for i, e in enumerate(employees["employee_id"]):
        emp[e] = employees["name"][i]
    ans = []
    for k in d:
        if len(d[k]) >= 3:
            if d[k][-3][-1] < d[k][-2][-1] < d[k][-1][-1]:
                ds = d[k][-1][-1] - d[k][-3][-1]
                #print(k, emp[k], ds)
                ans.append([k, emp[k], ds])
    ans.sort(key=lambda x: (-x[2], x[1]))
    print(ans)
    employees["improvement_score"] = employees["employee_id"]
    cnt = 0
    for a in ans:
        employees["employee_id"][cnt] = a[0]
        employees["name"][cnt] = a[1]
        employees["improvement_score"][cnt] = a[2]
        cnt += 1

    return pd.DataFrame(employees, columns=["employee_id", "name", "improvement_score"]).head(len(ans))
