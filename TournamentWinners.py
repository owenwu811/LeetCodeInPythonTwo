
#1194
#Hard

#The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.

#Write a solution to find the winner in each group.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#get all the group ids in one dictionary, and then add up all the players with their total scores in another

import pandas as pd

def tournament_winners(players: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, p in enumerate(players["group_id"]):
        d[p].append(players["player_id"][i])
    score = defaultdict(int)
    for i, m in enumerate(matches["first_player"]):
        score[m] += matches["first_score"][i]
    for i, m in enumerate(matches["second_player"]):
        score[m] += matches["second_score"][i]
    print(score)
    #ans = []
    one = []
    two = []
    for k in d:
        cur = []
        biggest = -1
        for a in d[k]:
            if a in score:
                if score[a] != 0:
                    cur.append([score[a], a])
                    biggest = max(biggest, a)
        cur.sort(key=lambda x: (x[0], -x[1]))
        print(k, cur, biggest)
        #ans.append([k, cur[-1][-1]])
        one.append(k)
        two.append(cur[-1][-1])
    res = pd.DataFrame()
    res["group_id"] = one
    res["player_id"] = two
    return res
