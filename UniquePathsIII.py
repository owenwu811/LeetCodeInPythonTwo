#980
#Hard

#You are given an m x n integer array grid where grid[i][j] could be:

#1 representing the starting square. There is exactly one starting square.
#2 representing the ending square. There is exactly one ending square.
#0 representing empty squares we can walk over.
#-1 representing obstacles that we cannot walk over.
#Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

#my own solution using python3:

#get all the non obstacle cells and make a dictionary, and then do a dfs comparing the exact same

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.non = []
        self.key = Counter()
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b] != -1:
                    self.non.append([a, b])
                    self.key[(a, b)] += 1
        print(self.non, "non")
        print(self.key)
        self.res = 0
        def dfs(i, j, cur):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1 or [i, j] in cur:
                return 
            if grid[i][j] == 2:
                now = Counter()
                for c in cur:
                    now[tuple(c)] += 1
                now[(i, j)] += 1
                if len(cur) == len(self.non) - 1 and now == self.key:
                    print(cur, "HA")
                    self.res += 1
                return
            cur.append([i, j])
            dfs(i + 1, j, cur)
            dfs(i - 1, j, cur)
            dfs(i, j + 1, cur)
            dfs(i, j - 1, cur)
            cur.pop()
            
        for i in range(len(grid)):
            for j in range(len(grid[i])): 
                if grid[i][j] == 1:
                    dfs(i, j, [])
        return self.res
