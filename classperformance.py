
#2989
#medium

#Write a solution to calculate the difference in the total score (sum of all 3 assignments) between the highest score obtained by students and the lowest score obtained by them.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#follow the picture exactly

import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    #first, second, third = scores["assignment1"], scores["assignment2"], scores["assignment3"]
    #print(first, second, third)
    first = []
    second = []
    third = []
    for i, a in enumerate(scores["assignment1"]):
        #print(a)
        first.append(a)
    for i, a in enumerate(scores["assignment2"]):
        second.append(a)
    for i, a in enumerate(scores["assignment3"]):
        third.append(a)
    print(first, second, third)
    i = 0
    diff = []
    while i < len(first):
        tot = first[i] + second[i] + third[i]
        diff.append(tot)

        i += 1
    print(diff)
    ans = max(diff) - min(diff)
    print(ans)
    scores["difference_in_score"] = ans
    return pd.DataFrame(scores, columns=["difference_in_score"]).head(1)
