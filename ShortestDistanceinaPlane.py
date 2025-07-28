#612
#medium

#The distance between two points p1(x1, y1) and p2(x2, y2) is sqrt((x2 - x1)2 + (y2 - y1)2).

#Write a solution to report the shortest distance between any two points from the Point2D table. Round the distance to two decimal points.

#The result format is in the following example.

#my own solution using python3:

#get all the points and the distance between them

import pandas as pd

def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, v in enumerate(point2_d["x"]):
        x, y = point2_d["x"][i], point2_d["y"][i]
        cur.append([x, y])
    ans = float('inf')
    for a in cur:
        for b in cur:
            if a != b:
                print(a, b)
                ans = min(ans, round(dist(a, b), 2))
    print(ans)
    res = pd.DataFrame()
    res["shortest"] = [ans]
    return res
