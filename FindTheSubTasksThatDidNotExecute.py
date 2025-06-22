
#1767
#hard

#Write a solution to report the IDs of the missing subtasks for each task_id.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#follow the instructions

import pandas as pd

def find_subtasks(tasks: pd.DataFrame, executed: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    for i, t in enumerate(tasks["task_id"]):
        d[t] = list(range(1, tasks["subtasks_count"][i] + 1))
    for i, e in enumerate(executed["task_id"]):
        for a in d[e]:
            if executed["subtask_id"][i] in d[e]:
                d[e].remove(executed["subtask_id"][i])
    print(d)
    ans = []
    for k in d:
        for a in d[k]:
            ans.append([k, a])
    print(ans)
    first = []
    second = []
    for a in ans:
        first.append(a[0])
        second.append(a[1])

    res = pd.DataFrame()
    res["task_id"] = first
    res["subtask_id"] = second
    #c#nt = 0
    #f#or a in ans:
     #   res["task_id"][cnt] = a[0]
    #    res["subtask_id"][cnt] = a[1]
    #    cnt += 1
    return res
