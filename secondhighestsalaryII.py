#3338
#medium

#Write a solution to find the employees who earn the second-highest salary in each department. If multiple employees have the second-highest salary, include all employees with that salary.

#Return the result table ordered by emp_id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#follow the instructions exactly

import pandas as pd

def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(employees["salary"]):
        #if v not in d[employees["dept"][i]]:
        d[employees["dept"][i]].append(v)
        d[employees["dept"][i]].sort()
    #print(d)
    sh = defaultdict(int)
    for k in d:
        if len(d[k]) >= 2:
            sh[k] = d[k][-2]
        else:
            sh[k] = d[k][-1]
    #print(sh)
    fd = dict()
    for k in d:
        #print(sh[k], k, d[k])
        biggest = d[k][-1]
        bl = bisect_left(d[k], biggest) - 1
        #print(bl)
        if bl >= 0 and bl < len(d[k]):
            target = d[k][bl]
            #print(target)
            fd[k] = target
    #print(fd)
    ansd = dict()
    for f in fd:
        key, val = f, fd[f]
        for i, e in enumerate(employees["emp_id"]):
            if employees["dept"][i] == key and employees["salary"][i] == val:
                ansd[employees["emp_id"][i]] = employees["dept"][i]
    print(ansd)
    a = list(ansd.items())
    print(a)
    a.sort(key=lambda x: x[0])
    for i, e in enumerate(employees["emp_id"]):
        if i < len(a):
            employees["emp_id"][i] = a[i][0]
            employees["dept"][i] = a[i][1]

    
        


    


    return pd.DataFrame(employees, columns=["emp_id", "dept"]).head(len(ansd))
