
#569
#Hard

#Write a solution to find the rows that contain the median salary of each company. While calculating the median, when you sort the salaries of the company, break the ties by id.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#for each list, get the median as even or odd length, and then group back with ids to get the lowest id as the triple combination

import pandas as pd

def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, c in enumerate(employee["company"]):
        d[c].append(employee["salary"][i])
        d[c].sort()
    print(d)
    ansd = defaultdict(list)
    for k in d:
        if len(d[k]) % 2 == 0:
            mid = len(d[k]) // 2
            ansd[k] = [d[k][mid - 1], d[k][mid]]
        else:
            mid = len(d[k]) // 2
            ansd[k] = [d[k][mid]]
    ans = []
    for a in ansd:
        for i, e in enumerate(employee["company"]):
            if e == a and employee["salary"][i] in ansd[a]:
                ans.append([employee["id"][i], e, employee["salary"][i]])
    print(ans)
    ans.sort()
    fd = defaultdict(list)
    for a in ans:
        b, c = a[1], a[2]
        fd[(b, c)].append(a[0])
        fd[(b, c)].sort()
    print(fd)
    ans = []
    for f in fd:
        one, two, three = f[0], f[1], fd[f][0]
        ans.append([one, two, three])
    print(ans)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["id"] = one
    res["company"] = two
    res["salary"] = three
    return res
