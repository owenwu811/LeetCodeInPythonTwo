
#2004
#Hard

#A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

#Hiring the largest number of seniors.
#After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.
#Write a solution to find the number of seniors and juniors hired under the mentioned criteria.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#sort each list, and then get the cheapest until you can't for each category

import pandas as pd

def count_seniors_and_juniors(candidates: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, c in enumerate(candidates["experience"]):
        d[c].append(candidates["salary"][i])
        d[c].sort()
    b = 70000
    sc = 0
    while d["Senior"] and b - d["Senior"][0] > 0:
        b -= d["Senior"][0]
        sc += 1
        del d["Senior"][0]
    jc = 0
    while d["Junior"] and b - d["Junior"][0] > 0:
        b -= d["Junior"][0]
        jc += 1
        del d["Junior"][0]
    print(sc, jc)
    res = pd.DataFrame()
    res["experience"] = ["Senior", "Junior"]
    res["accepted_candidates"] = [sc, jc]
    return res
