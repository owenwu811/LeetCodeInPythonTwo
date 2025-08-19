#1126
#medium

#The average activity for a particular event_type is the average occurrences across all companies that have this event.

#An active business is a business that has more than one event_type such that their occurrences is strictly greater than the average activity for that event.

#Write a solution to find all active businesses.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#gather the averages of each event type before looping through again and counting all business ids that are higher than the average, and then get those that do this more than once

import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    avg = defaultdict(list)
    for i, e in enumerate(events["event_type"]):
        avg[e].append(events["occurrences"][i])
    cnt = defaultdict(int)
    for a in avg:
        tot = mean(avg[a])
        print(a, tot)
        for i, e in enumerate(events["occurrences"]):
            if events["event_type"][i] == a:
                if e > tot:
                    print(events["business_id"][i])
                    cnt[events["business_id"][i]] += 1
    ans = []
    for c in cnt:
        if cnt[c] > 1:
            ans.append(c)
    res = pd.DataFrame()
    res["business_id"] = ans
    return res
