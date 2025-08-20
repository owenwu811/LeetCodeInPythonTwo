#1212
#medium

#You would like to compute the scores of all teams after all matches. Points are awarded as follows:
#A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
#A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
#A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
#Write a solution that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

#Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.

#The result format is in the following example.

#my own solution using python3:

#gather all the conditions of winning, losing, and tie, and then sort by the order as instructed

import pandas as pd

def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, m in enumerate(matches["host_team"]):
        if matches["host_goals"][i] > matches["guest_goals"][i]:
            d[m] += 3
        elif matches["host_goals"][i] < matches["guest_goals"][i]:
            d[matches["guest_team"][i]] += 3
        elif matches["host_goals"][i] == matches["guest_goals"][i]:
            d[m] += 1
            d[matches["guest_team"][i]] += 1
    for i, t in enumerate(teams["team_id"]):
        if t not in d:
            d[t] = 0
    m = dict()
    for i, t in enumerate(teams["team_id"]):
        m[t] = teams["team_name"][i]
    ans = []
    for k in d:
        #print(k, d[k])
        ans.append([k, d[k]])
    ans.sort(key=lambda x: x[1], reverse=True)
    print(ans)
    res = []
    for a in ans:
        res.append([a[0], m[a[0]], a[1]])
    res.sort(key=lambda x: (-x[2], x[0]))
    one, two, three = [], [], []
    for r in res:
        one.append(r[0])
        two.append(r[1])
        three.append(r[2])
    f = pd.DataFrame()
    f["team_id"] = one
    f["team_name"] = two
    f["num_points"] = three
    return f
