
#1783
#medium

#Write a solution to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#iterate through all cells to find all the player ids, and then use a dictionary to map the player ids frequency to the player name

import pandas as pd

def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    seen = set()
    for i, c in enumerate(championships["year"]):
        seen.add(championships["Wimbledon"][i])
        seen.add(championships["Fr_open"][i])
        seen.add(championships["US_open"][i])
        seen.add(championships["Au_open"][i])
    d = defaultdict(int)
    print(seen)
    players["grand_slams_count"] = players["player_id"]
    for i, p in enumerate(players["player_id"]):
        for j, c in enumerate(championships["Wimbledon"]):
            if c == p:
                #print(p, i)
                #print(players["player_name"][i])
                d[players["player_name"][i]] += 1
        for j, c in enumerate(championships["Fr_open"]):
            if c == p:
                #print(p, i)
                #print(players["player_name"][i])
                d[players["player_name"][i]] += 1
        for j, c in enumerate(championships["US_open"]):
            if c == p:
                #print(p, i)
                #print(players["player_name"][i])
                d[players["player_name"][i]] += 1
        for j, c in enumerate(championships["Au_open"]):
            if c == p:
                #print(p, i)
                #print(players["player_name"][i])
                d[players["player_name"][i]] += 1

             
    print(d)
    for i, p in enumerate(players["player_name"]):
        players["grand_slams_count"][i] = d[p]

    return pd.DataFrame(players, columns=["player_id", "player_name", "grand_slams_count"]).head(len(seen))
