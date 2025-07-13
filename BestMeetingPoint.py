#296
#Hard


#Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

#The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

#The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.


#my own solution using python3:

#just follow the instructions

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ans = 0
        co = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    co.append([i, j])
        x, y= [], []
        for c in co:
            x.append(c[0])
            y.append(c[1])
        x.sort()
        y.sort()
        first = int(median(x))
        second = int(median(y))
        now = [first, second]
        print(now)
        for i in range(len(co)):
            first = abs(now[1] - co[i][1])
            second = abs(now[0] - co[i][0])
            cur = dist(now, co[i])
            print(cur)
            ans += (first + second)
        return int(ans)
