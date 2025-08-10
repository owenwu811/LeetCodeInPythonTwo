#1308
#medium

#Write a solution to find the total score for each gender on each day.

#Return the result table ordered by gender and day in ascending order.

#The result format is in the following example.

#my own solution using python3:

#get each gender, and order by date, and then accumulate

import pandas as pd

def running_total(scores: pd.DataFrame) -> pd.DataFrame:
    fem = defaultdict(list)
    men = defaultdict(list)
    for i, s in enumerate(scores["gender"]):
        if s == 'F':
            fem[s].append([scores["day"][i], scores["score_points"][i], scores["player_name"][i]])
            fem[s].sort()
        else:
            men[s].append([scores["day"][i], scores["score_points"][i], scores["player_name"][i]])
            men[s].sort()
    ftot = 0
    mentot = 0
    ans = []
    for f in fem:
        #print(f, fem[f])
        for a in fem[f]:
            ftot += a[1]
            #print(a, ftot)
            ts = str(a[0]).split(" ")[0]
            ans.append(["F", ts, ftot])
    for m in men:
        for a in men[m]:
            mentot += a[1]
            #print(a, mentot)
            ts = str(a[0]).split(" ")[0]
            ans.append(["M", ts, mentot])
    ans.sort(key=lambda x: (x[0], x[1]))
    print(ans)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["gender"] = one
    res["day"] = two
    res["total"] = three
    return res
