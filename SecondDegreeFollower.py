#614
#medium

#A second-degree follower is a user who:

#follows at least one user, and
#is followed by at least one user.
#Write a solution to report the second-degree users and the number of their followers.

#Return the result table ordered by follower in alphabetical order.

#The result format is in the following example.

#my own solution using python3:

#use the key as the person being followed and append to the value list all people who follow the person key, and then just check for each condition of being followed and following

import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    ans = []
    for i, f in enumerate(follow["followee"]):
        d[f].append(follow["follower"][i])
    for k in d:
        #print(k, d[k])
        follows = False
        for a in d:
            if a != k:
                for nei in d[a]:
                    if k == nei:
                        follows = True
                        break
        if follows and len(d[k]) >= 1:
            ans.append([k, len(d[k])])
    ans.sort()
    print(ans)
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["follower"] = one
    res["num"] = two
    return res
