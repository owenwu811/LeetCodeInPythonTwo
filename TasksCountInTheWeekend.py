#2298
#medium

#Write a solution to report:

#the number of tasks that were submitted during the weekend (Saturday, Sunday) as weekend_cnt, and
#the number of tasks that were submitted during the working days as working_cnt.
#Return the result table in any order.

#The result format is shown in the following example.



#my own solution using python3:

#use dt.day_name()

import pandas as pd

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    cur = list(tasks["submit_date"].dt.day_name())
    print(cur)
    d = defaultdict(int)
    for i, t in enumerate(tasks["task_id"]):
        if cur[i] == "Saturday" or cur[i] == "Sunday":
            d["weekend"] += 1
        else:
            d["weekday"] += 1
    print(d)
    res = pd.DataFrame()
    res["weekend_cnt"] = [d["weekend"]]
    res["working_cnt"] = [d["weekday"]]
    return res

    
