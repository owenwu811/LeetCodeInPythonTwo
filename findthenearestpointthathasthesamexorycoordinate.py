#1779
#easy

#You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

#Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

#The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

 

#Example 1:

#Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
#Output: 2
#Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.


#my own solution using python3:

#simulate the process with a sorted dictionary

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        startx, starty = x, y
        smallestdist = float('inf')
        d = defaultdict(list)
        for i, p in enumerate(points):
            curx, cury = p[0], p[1]
            
            xdiff, ydiff = abs(curx - startx), abs(cury - starty)
            totdist = xdiff + ydiff
            smallestdist = min(smallestdist, totdist)
            d[totdist].append([i, curx, cury])
        d = dict(sorted(d.items(), key=lambda x: (x[0], x[1][0])))
        print(d)
        if not d:
            return -1
        for k in d:
            for c in d[k]:
                print(c)
                if c[1] == startx or c[2] == starty:
                    return c[0]
        return -1
            
