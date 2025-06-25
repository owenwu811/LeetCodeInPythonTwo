

#2010
#Hard

#A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

#Keep hiring the senior with the smallest salary until you cannot hire any more seniors.
#Use the remaining budget to hire the junior with the smallest salary.
#Keep hiring the junior with the smallest salary until you cannot hire any more juniors.
#Write a solution to find the ids of seniors and juniors hired under the mentioned criteria.

#Return the result table in any order.


#my own solution using python3:

#keep two lists for seniors and juniors, sort them, and then keep popping left until you can't

import pandas as pd

def number_of_joiners(candidates: pd.DataFrame) -> pd.DataFrame:
    budget = 70000
    seniors, juniors = [], []
    for i, c in enumerate(candidates["salary"]):
        if candidates["experience"][i] == "Junior":
            juniors.append(c)
        else:
            seniors.append(c)
    juniors.sort()
    seniors.sort()
    juniors = deque(juniors)
    seniors = deque(seniors)
    ans = []
    while seniors and budget - seniors[0] > 0:
        a = seniors.popleft()
        print(a)
        ans.append(a)
        budget -= a
    while juniors and budget - juniors[0] > 0:
        a = juniors.popleft()
        print(a)
        ans.append(a)
        budget -= a
    f = []
    for i, c in enumerate(candidates["salary"]):
        if c in ans:
            f.append(candidates["employee_id"][i])
    print(f)
    res = pd.DataFrame()
    res["employee_id"] = f
    return res

