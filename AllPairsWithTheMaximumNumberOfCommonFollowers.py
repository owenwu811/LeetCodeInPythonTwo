#1951
#medium

#Write a solution to find all the pairs of users with the maximum number of common followers. In other words, if the maximum number of common followers between any two users is maxCommon, then you have to return all pairs of users that have maxCommon common followers.

#The result table should contain the pairs user1_id and user2_id where user1_id < user2_id.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#try all the combinations of pairs, and find how many intersecting elements using set, and then loop again to see which one satisifes the biggest intersecting number

import pandas as pd

def find_pairs(relations: pd.DataFrame) -> pd.DataFrame:
    foll = defaultdict(set)
    for i, r in enumerate(relations["user_id"]):
        foll[r].add(relations["follower_id"][i])
    commonnum = defaultdict(int)
    cur = list(foll.keys())
    biggest = float('-inf')
    for c in cur:
        for a in cur:
            if a != c:
                tot = len(foll[a].intersection(foll[c]))
                biggest = max(biggest, tot)
    ans = []
    for c in cur:
        for a in cur:
            if a != c:
                now = len(foll[a].intersection(foll[c]))
                if now == biggest and [a, c] not in ans:
                    ans.append([c, a])
    print(ans)
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["user1_id"] = one
    res["user2_id"] = two
    return res
