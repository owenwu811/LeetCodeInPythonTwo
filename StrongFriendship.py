#1949
#medium

#A friendship between a pair of friends x and y is strong if x and y have at least three common friends.

#Write a solution to find all the strong friendships.

#Note that the result table should not contain duplicates with user1_id < user2_id.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#get friends from 1 and 2 as undirected graph, and find intersection of length atleast 3 or greater

import pandas as pd

def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    ans = []
    for i, f in enumerate(friendship["user1_id"]):
        d[f].append(friendship["user2_id"][i])
        d[friendship["user2_id"][i]].append(f)
    for i, f in enumerate(friendship["user1_id"]):
        cur = d[f]
        second = d[friendship["user2_id"][i]]
        #print(cur, second)
        together = set(cur).intersection(set(second))
        if len(together) >= 3:
            print(f, friendship["user2_id"][i], together)
            ans.append([f, friendship["user2_id"][i], len(together)])
    res = pd.DataFrame()
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res["user1_id"] = one
    res["user2_id"] = two
    res["common_friend"] = three
    return res
