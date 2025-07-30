#2978
#medium

#Two coordindates (X1, Y1) and (X2, Y2) are said to be symmetric coordintes if X1 == Y2 and X2 == Y1.

#Write a solution that outputs, among all these symmetric coordintes, only those unique coordinates that satisfy the condition X1 <= Y1.

#Return the result table ordered by X and Y (respectively) in ascending order.

#The result format is in the following example.

#my own solution using python3:

#get all pairs, and then loop through to check each condition, and then sort each sublist and the entire matrix

import pandas as pd

def symmetric_pairs(coordinates: pd.DataFrame) -> pd.DataFrame:
    pairs = []
    for i, c in enumerate(coordinates["X"]):
        pairs.append([c, coordinates["Y"][i]])
    ans = []
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if pairs[i][0] == pairs[j][1] and pairs[i][1] == pairs[j][0]:
                if pairs[i][0] <= pairs[j][1]:
                    #print(pairs[i])
                    if sorted(pairs[i]) not in ans:
                        ans.append(sorted(pairs[i]))
    #ans.sort(key=lambda x: (x[0], x[1]))
    ans.sort()
    print(ans)
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["x"] = one
    res["y"] = two
    return res
