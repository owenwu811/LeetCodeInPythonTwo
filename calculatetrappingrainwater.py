
#3061
#hard

#Write a solution to calculate the amount of rainwater can be trapped between the bars in the landscape, considering that each bar has a width of 1 unit.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#use the same two pointer technique for trapping rain water

import pandas as pd

def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, v in enumerate(heights["height"]):
        cur.append(v)
    print(cur)
    l, r = 0, len(cur) - 1
    maxleft, maxright = cur[l], cur[r]
    ans = 0
    while l < r:
        if cur[l] < cur[r]:
            #maxleft = max(maxleft, cur[l])
            l += 1
            maxleft = max(maxleft, cur[l])
            ans += (maxleft - cur[l])
            
        else:
            r -= 1
            maxright = max(maxright, cur[r])
            ans += (maxright - cur[r])
        print(maxleft, maxright)




    heights["total_trapped_water"] = ans
    return pd.DataFrame(heights, columns=["total_trapped_water"]).head(1)
