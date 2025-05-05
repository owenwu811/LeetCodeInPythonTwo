#2510
#medium

#You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1).

#Return true if there is a path from (0, 0) to (m - 1, n - 1) that visits an equal number of 0's and 1's. Otherwise return false.

#Input: grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]
#Output: true
#Explanation: The path colored in blue in the above diagram is a valid path because we have 3 cells with a value of 1 and 3 with a value of 0. Since there is a valid path, we return true.

#my own solution using python3:

#use dfs from top right to bottom left

class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        self.flag = False
        zc, oc = 0, 0
        self.m = len(grid)
        self.n = len(grid[0])
        @cache
        #[[0,1,0,0],
        #[0,0,0,0],
        #[0,0,1,1]]
        def dfs(row, col, zc, oc):
            #print(row, col, zc, oc)
            
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
                return 
            #if row == len(grid) - 1 and col == len(grid[row]) - 1:
            #    print(row, col, "done")
            #    if zc == oc:
            #        self.flag = True
            #    return 
            #print(row, col, zc, oc)
            if grid[row][col] == 0:
                zc += 1
            if grid[row][col] == 1:
                oc += 1
            #print(row, col, zc, oc)
            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                #print(row, col, "done")
                if zc == oc:
                    self.flag = True
                return 
            dfs(row + 1, col, zc, oc)
            dfs(row, col + 1, zc, oc)
            
        
        dfs(0, 0, zc, oc)
       
        return self.flag
