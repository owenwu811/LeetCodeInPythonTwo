#615
#Hard

#Find the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#messy but working

import pandas as pd

def average_salary(salary: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, s in enumerate(salary["pay_date"]):
        cur = str(s).split(" ")[0]
        d[cur].append(salary["amount"][i])
    avg = dict()
    for k in d:
        curavg = sum(d[k]) / len(d[k])
        avg[k] = curavg
    ans = defaultdict(list)
    for i, e in enumerate(employee["department_id"]):
        eid = employee["employee_id"][i]
        for i, s in enumerate(salary["employee_id"]):
            if eid == s:
                cursal = salary["amount"][i]
                dd = str(salary["pay_date"][i]).split(" ")[0]
                ans[(dd, e)].append(cursal)
    res = []
    for a in ans:
        ca = sum(ans[a]) / len(ans[a])
        kk = avg[a[0]]
        if ca > kk:
            if [a[0], a[1], "higher"] not in res:
                res.append([a[0], a[1], "higher"])
        elif ca == kk:
            if [a[0], a[1], "same"] not in res:
                res.append([a[0], a[1], "same"])
        else:
            if [a[0], a[1], "lower"] not in res:
                res.append([a[0], a[1], "lower"])
    print(res)
    one, two, three = [], [], []
    used = set()
    for r in res:
        if (r[0][:-3], r[1]) in used:
            continue
        one.append(r[0][:-3])
        two.append(r[1])
        three.append(r[2])
        used.add((r[0][:-3], r[1]))
    print(one)
    final = pd.DataFrame()
    final["pay_month"] = one
    final["department_id"] = two
    final["comparison"] = three
    return final
