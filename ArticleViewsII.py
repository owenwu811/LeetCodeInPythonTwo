#1149
#medium

#Write a solution to find all the people who viewed more than one article on the same date.

#Return the result table sorted by id in ascending order.

#The result format is in the following example.

#my own solution using python3:

#get all the viewdates and viewer ids as the key, and just see how many article ids are associated with that combo without including duplicates

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(set)
    for i, v in enumerate(views["viewer_id"]):
        viewdat = views["view_date"][i]
        d[(v, viewdat)].add(views["article_id"][i])
    ans = []
    for k in d:
        print(k, d[k])
        if len(d[k]) >= 2:
            if k[0] not in ans:
                ans.append(k[0])
    ans.sort()
    res = pd.DataFrame()
    res["id"] = ans
    return res
