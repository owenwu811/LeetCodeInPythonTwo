#2314
#medium

#Write a solution to report the day that has the maximum recorded degree in each city. If the maximum degree was recorded for the same city multiple times, return the earliest day among them.

#Return the result table ordered by city_id in ascending order.

#The result format is shown in the following example.

#my own solution using python3:

#use several dictionaries to get one piece of information in each loop

import pandas as pd

def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, w in enumerate(weather["city_id"]):
        d[w].append(weather["degree"][i])
        d[w].sort()
    dd = defaultdict(int)
    for k in d:
        dd[k] = max(d[k])
    print(d)
    cur = defaultdict(list)
    for i, w in enumerate(weather["city_id"]):
        if weather["degree"][i] == dd[w]:
            now = str(weather["day"][i]).split(" ")[0]
            cur[w].append([now, w, weather["degree"][i]])
            cur[w].sort()
    print(cur)
    ans = []
    for c in cur:
        good = cur[c][0]
        ans.append(good)
    ans.sort(key=lambda x: (x[1]))
    print(ans)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["city_id"] = two
    res["day"] = one
    res["degree"] = three
    return res


