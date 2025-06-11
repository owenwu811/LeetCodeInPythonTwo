
#1285
#medium

#Write a solution to find the start and end number of continuous ranges in the table Logs.

#Return the result table ordered by start_id.

#The result format is in the following example.


#my own solution using python3:

#loop through the array to find the biggest and smallest numbers, and then edit each column accordingly, only displaying the length of the list you created from the top

import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    tot = []
    cur = []
    for i, a in enumerate(logs["log_id"]):
        if not cur:
            cur.append(a)
        else:
            if a == cur[-1] + 1:
                cur.append(a)
            else:
                tot.append(cur.copy())
                cur.clear()
                cur.append(a)
    tot.append(cur)
    print(tot)
    logs["start_id"] = logs["log_id"]
    logs["end_id"] = logs["log_id"]
    for i in range(len(tot)):
        logs["start_id"][i] = tot[i][0]
        logs["end_id"][i] = tot[i][-1]
    return pd.DataFrame(logs, columns=["start_id", "end_id"]).head(len(tot))
