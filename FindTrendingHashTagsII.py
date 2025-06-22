
#3103
#Hard

#Write a solution to find the top 3 trending hashtags in February 2024. Every tweet may contain several hashtags.

#Return the result table ordered by count of hashtag, hashtag in descending order.

#The result format is in the following example.


#my own solution using python3:

#do exactly what the instructions say

import pandas as pd

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, v in enumerate(tweets["tweet"]):
        cur = v.split(" ")
        for c in cur:
            if c[0] == "#":
                #print(c)
                d[c] += 1
    d = list(d.items())
    d.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(d)
    tweets["hashtag"] = "a"
    tweets["count"] = 0
    cnt = 0
    for a in d:
        tweets["hashtag"][cnt] = a[0]
        tweets["count"][cnt] = a[1]
        cnt += 1
    return pd.DataFrame(tweets, columns=["hashtag", "count"]).head(3)
