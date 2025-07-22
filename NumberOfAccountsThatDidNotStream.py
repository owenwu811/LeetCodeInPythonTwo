#2020
#medium

#Write an SQL query to report the number of accounts that bought a subscription in 2021 but did not have any stream session.

#The query result format is in the following example.

#my own solution using python3:

#get all the account ids that include 2021, and then remove them if the streams table includes 2021 for that row

import pandas as pd

def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    good = []
    for i, s in enumerate(subscriptions["account_id"]):
        sd, ed = str(subscriptions["start_date"][i]).split(" ")[0], str(subscriptions["end_date"][i]).split(" ")[0]
        sd = sd.split("-")
        ed = ed.split("-")
        if sd[0] == "2021" or ed[0] == "2021":
            good.append(s)
    ans = []
    for g in good:
        for i, s in enumerate(streams["account_id"]):
            cur = str(streams["stream_date"][i]).split(" ")[0]
            cur = cur.split("-")
            #print(cur)
            if cur[0] == "2021":
                #print(s)
                if s in good:
                    good.remove(s)
    print(good)
    res = pd.DataFrame()
    res["accounts_count"] = [len(good)]
    return res
