#2041
#medium

#Write a solution to report the IDs of the candidates who have at least two years of experience and the sum of the score of their interview rounds is strictly greater than 15.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#do exactly as the instructions say

import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, r in enumerate(rounds["interview_id"]):
        d[r] += rounds["score"][i]
    print(d)
    ans = []
    for j, c in enumerate(candidates["interview_id"]):
        if candidates["years_of_exp"][j] >= 2:
            if d[candidates["interview_id"][j]] > 15:
                print(candidates["candidate_id"][j])
                ans.append(candidates["candidate_id"][j])
    cnt = 0
    for a in ans:
        candidates["candidate_id"][cnt] = a
        cnt += 1


    return pd.DataFrame(candidates, columns=["candidate_id"]).head(len(ans))
