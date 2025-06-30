
#3384
#Hard

#Write a solution to calculate the dominance score for each team in both halves of the match. The rules are as follows:

#A match is divided into two halves: first half (00:00-45:00 minutes) and second half (45:01-90:00 minutes)
#The dominance score is calculated based on successful and intercepted passes:
#When pass_to is a player from the same team: +1 point
#When pass_to is a player from the opposing team (interception): -1 point
#A higher dominance score indicates better passing performance
#Return the result table ordered by team_name and half_number in ascending order.

#The result format is in the following example.

#my own solution using python3:

#be careful of the cases between 45 and 46

import pandas as pd

def calculate_team_dominance(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    d = dict()
    for i, t in enumerate(teams["team_name"]):
        d[teams["player_id"][i]] = t
    dd = defaultdict(int)
    for i, p in enumerate(passes["pass_from"]):
        ts = passes["time_stamp"][i]
        f = int(ts[:2])
        s = int(ts[3:])
        tot = f + s
        print(f, s, tot)
        pf, pt = passes["pass_from"][i], passes["pass_to"][i]
        if f <= 45:
            if f == 45 and s > 0:
                if d[pf] == d[pt]:
                    print("same")
                    dd[(d[pf], 2)] += 1
                else:
                    print("diff")
                    dd[(d[pf], 2)] -= 1
            else:
                if d[pf] == d[pt]:
                    dd[(d[pf], 1)] += 1
                else:
                    print("diff")
                    dd[(d[pf], 1)] -= 1
        else:
            print(ts, "secondhalf")
            if d[pf] == d[pt]:
                print("same")
                dd[(d[pf], 2)] += 1
            else:
                print("diff")
                dd[(d[pf], 2)] -= 1
    #print(dd)
    ans = []
    for k in dd:
        f, t, th = k[0], k[1], dd[k]
        ans.append([f, t, th])
    ans.sort(key=lambda x: (x[0], x[1], x[2]))
    print(ans)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["team_name"] = one
    res["half_number"] = two
    res["dominance"] = three
    return res
