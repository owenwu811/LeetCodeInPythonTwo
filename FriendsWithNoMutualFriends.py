#3058
#medium

#Write a solution to find all pairs of users who are friends with each other and have no mutual friends.

#Return the result table ordered by user_id1, user_id2 in ascending order.

#The result format is in the following example.

#my own solution using python3:

#get each bidirectional relationship, and then loop again to see if there's any intersection

import pandas as pd

def friends_with_no_mutual_friends(friends: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, f in enumerate(friends["user_id1"]):
        d[f].append(friends["user_id2"][i])
        d[friends["user_id2"][i]].append(f)
    print(d)
    ans = []
    for i, f in enumerate(friends["user_id1"]):
        one, two = f, friends["user_id2"][i]
        tog = set(d[one]).intersection(set(d[two]))
        if not tog:
            print(one, two)
            ans.append([one, two])
        #print(tog)
    ans.sort()
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["user_id1"] = one
    res["user_id2"] = two
    return res
