#1811
#medium

#Write a solution to report the name and the mail of all interview candidates. A user is an interview candidate if at least one of these two conditions is true:

#The user won any medal in three or more consecutive contests.
#The user won the gold medal in three or more different contests (not necessarily consecutive).
#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#gather all the data from different tables, and sort and filter

import pandas as pd

def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    d, gold = defaultdict(list), defaultdict(set)
    cid = defaultdict(list)
    for i, c in enumerate(contests["contest_id"]):
        cid[c].append(contests["gold_medal"][i])
        gold[contests["gold_medal"][i]].add(contests["contest_id"][i])
        cid[c].append(contests["silver_medal"][i])
        cid[c].append(contests["bronze_medal"][i])
    consec = defaultdict(list)
    for i, u in enumerate(users["user_id"]):
        for k in cid:
            if u in cid[k]:
                consec[u].append(k)
                consec[u].sort()
    #print(consec)
    #print(gold)
    ans = []
    for g in gold:
        if len(gold[g]) >= 3:
            if g not in ans:
                ans.append(g)
    for c in consec:
        size = 3
        now = consec[c]
        for i in range(len(now) - 2):
            cur = now[i: i + 3]
            #print(cur)
            if cur[0] + 1 == cur[1] and cur[1] + 1 == cur[2]:
                if c not in ans: ans.append(c)
    print(ans)
    people = dict()
    for i, u in enumerate(users["user_id"]):
        if u in ans:
            people[u] = [users["mail"][i], users["name"][i]]
    one, two = [], []
    for p in people:
        print(p, people[p])
        one.append(people[p][0])
        two.append(people[p][1])
    res = pd.DataFrame()
    res["name"] = one
    res["mail"] = two
    return res
