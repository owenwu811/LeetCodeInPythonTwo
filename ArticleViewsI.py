#1148
#easy

#Write a solution to find all the authors that viewed at least one of their own articles.

#Return the result table sorted by id in ascending order.

#The result format is in the following example.


#my own solution using python3:

#just check if viewer id == authorid, and if so, include that number, and sort without duplicates

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ans = []
    for i, v in enumerate(views["author_id"]):
        if v == views["viewer_id"][i]:
            ans.append(v)
    ans = list(set(ans))
    ans.sort()
    res = pd.DataFrame()
    res["id"] = ans

    return res
