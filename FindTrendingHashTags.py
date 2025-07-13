
#3087
#medium

#Write a solution to find the top 3 trending hashtags in February 2024. Each tweet only contains one hashtag.

#Return the result table orderd by count of hashtag, hashtag in descending order.

#The result format is in the following example.


#my own solution using python3:

#since you can't sort a hashtag string in reverse order, sort it in normal order, and then reverse it, and then get the 1st three

import pandas as pd

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, t in enumerate(tweets["tweet"]):
        cur = t.split(" ")
        print(cur)
        for c in cur:
            if c:
                if c[0] == "#":
                    d[c] += 1
    ans = []
    for k in d:
        ans.append([k, d[k]])
    ans.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(ans)
    one, two = [], []
    for a in ans[:3]:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["HASHTAG"] = one
    res["HASHTAG_COUNT"] = two
    return res
