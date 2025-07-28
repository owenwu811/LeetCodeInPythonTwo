#3596
#medium

#You are given two integers m and n representing the number of rows and columns of a grid, respectively.

#The cost to enter cell (i, j) is defined as (i + 1) * (j + 1).

#The path will always begin by entering cell (0, 0) on move 1 and paying the entrance cost.

#At each step, you move to an adjacent cell, following an alternating pattern:

#On odd-numbered moves, you must move either right or down.
#On even-numbered moves, you must move either left or up.
#Return the minimum total cost required to reach (m - 1, n - 1). If it is impossible, return -1.

#my own solution using python3:

#use recursion to get all the paths depending on the conditions

class Solution:
    def minCost(self, m: int, n: int) -> int:
        self.ans = float('inf')
        def dfs(x, y, cnt, seen, turn):
            #print(x, y)
            if x < 0 or x >= m or y < 0 or y >= n or (x, y) in seen:
                return -1
            if x == m - 1 and y == n - 1:
                print(cnt, turn)
                self.ans = min(self.ans, cnt + turn)
                return cnt + turn
            turn += 1
            print(turn)
            seen.add((x, y))
            if turn % 2 != 0:
                fx, fy = x + 1, y
                sx, sy = x, y + 1
                first = dfs(fx, fy, (fx + 1) * (fy + 1), seen, turn)
                print(first, "first")
                second = dfs(sx, sy, (sx + 1) * (sy + 1), seen, turn)
                print(second, "second")
                
            else:
                fx, fy = x - 1, y
                sx, sy = x, y - 1
                first = dfs(fx - 1, fy, (fx + 1) * (sy + 1), seen, turn)
                second = dfs(sx, sy - 1, (fx + 1) * (sy + 1), seen, turn)
                
            return min(first, second) 
        dfs(0, 0, (0 + 1) * (0 + 1), set(), 0)
        if self.ans == float('inf'): return -1
        return self.ans
