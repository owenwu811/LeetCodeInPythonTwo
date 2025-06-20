#3057
#Hard

#Write a solution to find the employees who are allocated to projects with a workload that exceeds the average workload of all employees for their respective teams

#Return the result table ordered by employee_id, project_id in ascending order.

#The result format is in the following example.


#my own solution using python3:

#messy but working

import pandas as pd

def employees_with_above_avg_workload(project: pd.DataFrame, employees: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(employees["team"]):
        for j, a in enumerate(project["employee_id"]):
            if a == employees["employee_id"][i]:
                d[v].append(project["workload"][j])
    print(d)
    md = dict()
    for k in d:
        md[k] = mean(d[k])
    #print(md)
    ans = []
    for i, v in enumerate(employees["employee_id"]):
        for j, a in enumerate(project["employee_id"]):
            if v == a:
                if project["workload"][j] > md[employees["team"][i]]:
                    ans.append([employees["employee_id"][i], project["project_id"][i], employees["name"][i], project["workload"][j]])
    ans.sort(key=lambda x: (x[0], x[1]))
    print(ans)
    employees["EMPLOYEE_ID"] = project["project_id"]
    employees["PROJECT_ID"] = project["project_id"]
    employees["EMPLOYEE_NAME"] = employees["name"]
    employees["PROJECT_WORKLOAD"] = project["project_id"]
    cnt = 0

    for a in ans:
        employees["EMPLOYEE_ID"][cnt] = a[0]
        employees["PROJECT_ID"][cnt] = a[1]
        employees["EMPLOYEE_NAME"][cnt] = a[2]
        employees["PROJECT_WORKLOAD"][cnt] = a[3]

        cnt += 1


    return pd.DataFrame(employees, columns=["EMPLOYEE_ID", "PROJECT_ID", "EMPLOYEE_NAME", "PROJECT_WORKLOAD"]).head(len(ans))
