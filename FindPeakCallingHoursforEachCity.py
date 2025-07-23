
#2984
#medium

#Write a solution to find the peak calling hour for each city. If multiple hours have the same number of calls, all of those hours will be recognized as peak hours for that specific city.

#Return the result table ordered by peak calling hour and city in descending order.

#The result format is in the following example.

#my own solution using python3:

#get the number of calls for each hour by recording all calls, and then get the longest call per city, and then gather the results

import pandas as pd

def peak_calling_hours(calls: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    
    for i, c in enumerate(calls["call_time"]):
        cur = str(c).split(" ")[1][:2]
        #print(cur)
        d[(cur, calls["city"][i])].append(calls["caller_id"][i])
    dd = defaultdict(int)
    
    for k in d:
        #print(k, d[k])
        dd[k[1]] = max(dd[k[1]], len(d[k]))
    ans = []
    for k in d:
        if len(d[k]) == dd[k[1]]:
            print(k[1], k[0], dd[k[1]])
            ans.append([k[1], k[0], dd[k[1]]])

            #ans.append([k[1], k[1], dd[k[1]]])
    print(ans)
    ans.sort(key=lambda x: (x[1], x[0]), reverse=True)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(int(a[1]))
        three.append(a[2])
    res = pd.DataFrame()
    res["city"] = one
    res["peak_calling_hour"] = two
    res["number_of_calls"] = three
    return res
