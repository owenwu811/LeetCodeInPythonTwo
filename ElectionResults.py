#2820
#medium

#The election is conducted in a city where everyone can vote for one or more candidates or choose not to vote. Each person has 1 vote so if they vote for multiple candidates, their vote gets equally split across them. For example, if a person votes for 2 candidates, these candidates receive an equivalent of 0.5 votes each.

#Write a solution to find candidate who got the most votes and won the election. Output the name of the candidate or If multiple candidates have an equal number of votes, display the names of all of them.

#Return the result table ordered by candidate in ascending order.

#The result format is in the following example.

#my own solution using python3:

#see if the cell is null - if it is not, then add it into the size calculation

import pandas as pd

def get_election_results(votes: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(votes["voter"]):
        try:
            a = len(votes["candidate"][i])
            d[v].append(a)
        except:
            continue
    print(d)
    tally = defaultdict(int)
    biggest = float('-inf')
    for i, v in enumerate(votes["candidate"]):
        try:
            a = len(votes["voter"][i])
            size = len(d[votes["voter"][i]])
            #print(size)
            tot = 1 / size
            tally[v] += tot
            biggest = max(biggest, tally[v])

        except:
            continue
    print(tally)
    ans = []
    for t in tally:
        if tally[t] == biggest:
            ans.append(t)
    ans.sort()
    res = pd.DataFrame()
    res["candidate"] = ans
    return res

