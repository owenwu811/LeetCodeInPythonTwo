
#3567
#medium

#You are given an m x n integer matrix grid and an integer k.

#For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

#Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

#Note: If all elements in the submatrix have the same value, the answer will be 0.

#A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
 

#Example 1:

#Input: grid = [[1,8],[3,-2]], k = 2

#Output: [[2]]

#Explanation:

#There is only one possible k x k submatrix: [[1, 8], [3, -2]].
#Distinct values in the submatrix are [1, 8, 3, -2].
#The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].


#my own solution using python3:

#just brute force 

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #[[1,-2,3],
        #[2,3,5]]
        taken = []
        ans = []
        for i in range(len(grid)):
            r = []
            for j in range(len(grid[0])):
                if i + k - 1 < len(grid) and j + k - 1 < len(grid[0]):
                    now = SortedSet()
                    for x in range(i, i + k):
                        for y in range(j, j + k):
                            curval = grid[x][y]
                            now.add(curval)
                    print(now)
                    cc = float('inf')
                    for u in range(1, len(now)):
                        print(now[u - 1], now[u])
                        cc = min(cc, abs(now[u] - now[u - 1]))
                        if u < len(now) - 1:
                            cc = min(cc, abs(now[u] - now[u + 1]))

                    if cc == float('inf'):
                        r.append(0)
                    else:
                        r.append(cc)
            if r:
                ans.append(r.copy())
        return ans
