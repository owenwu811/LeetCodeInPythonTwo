#1219
#medium

#In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

#Return the maximum amount of gold you can collect under the conditions:

#Every time you are located in a cell you will collect all the gold in that cell.
#From your position, you can walk one step to the left, right, up, or down.
#You can't visit the same cell more than once.
#Never visit a cell with 0 gold.
#You can start and stop collecting gold from any position in the grid that has some gold.


#my own solution using python3:

#do a dfs on cells without 0, and calculate the best from each direction without visiting the same cell more than once

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0
        def dfs(i, j, cur, seen):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == "v":
                return 
            cur.append(grid[i][j])
            #print(cur)
            orig = grid[i][j]
            grid[i][j] = "v"
            self.ans = max(self.ans, sum(cur))
            seen.add((i, j))
            down = dfs(i + 1, j, cur, seen)
            up = dfs(i - 1, j, cur, seen)
            right = dfs(i, j + 1, cur, seen)
            left = dfs(i, j - 1, cur, seen)
            grid[i][j] = orig
            cur.pop()
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    dfs(i, j, [], set())
        return self.ans
