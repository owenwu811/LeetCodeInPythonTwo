

#100650 (may 10, 2025 contest) ama 3546

#medium

#You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

#Each of the two resulting sections formed by the cut is non-empty.
#The sum of the elements in both sections is equal.
#Return true if such a partition exists; otherwise return false.

 

#Example 1:

#Input: grid = [[1,4],[2,3]]

#Output: true

#Explanation:

#my own solution using python3:

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        tot = 0
        for g in grid:
            tot += sum(g)
        cur = 0
        for g in grid:
            cur += sum(g)
            #print(cur, tot)
            if cur == tot - cur:
                return True
        start = 0
        cols = []
        totc = 0
        while start < len(grid[0]):
            curcol = []
            for j in range(len(grid)):
                print(j, start)
                curcol.append(grid[j][start])
            start += 1
            cols.append(curcol)
            totc += sum(curcol)
        curc = 0
        for c in cols:
            curc += sum(c)
            if curc == totc - curc:
                return True
        return False
