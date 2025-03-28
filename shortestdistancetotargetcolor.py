
#1182
#medium

#You are given an array colors, in which there are three colors: 1, 2 and 3.

#You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

 

#Example 1:

#Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
#Output: [3,0,3]
#Explanation: 
#The nearest 3 from index 1 is at index 4 (3 steps away).
#The nearest 2 from index 2 is at index 2 itself (0 steps away).
#The nearest 1 from index 6 is at index 3 (3 steps away).


#my own solution using python3:

#use binary search on indicies to find closest value

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        d = defaultdict(list)
        for i, c in enumerate(colors):
            d[c].append(i)
        colorset = set(colors)
        for q in queries:
            idx, target = q[0], q[1]
            if target not in colorset:
                res.append(-1)
                print("done")
                continue
            cur = float('inf')
            #print(idx, d[target])
            b = bisect_left(d[target], idx)
            #print(b, d[target], "b", idx)
            
            if b >= len(d[target]):
                print(idx, d[target][-1], "right")
                cur = min(cur, idx - d[target][-1])
            elif b < 0:
                print(idx, d[target][0], "left")
                cur = min(cur, d[target][0] - idx)
            else:
                if b - 1 >= 0:
                    print(idx, d[target][b - 1], "onel")
                    cur = min(cur, idx - d[target][b - 1])
                if b + 1 < len(d[target]):
                    print(idx, d[target][b + 1], "onrr")
                    cur = min(cur, d[target][b + 1] - idx)
                if b >= 0 and b < len(d[target]):
                    print(idx, d[target][b], "center")
                    cur = min(cur, abs(idx - d[target][b]))

                
            
            #for a in d[target]:
            #    cur = min(cur, abs(idx - a))
            res.append(cur)
        return res
