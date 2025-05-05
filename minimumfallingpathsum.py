
#931
#medium

#Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

#A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

#Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
#Output: 13
#Explanation: There are two falling paths with a minimum sum as shown.


#my own solution using python3:

#tabulate the solution

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix.copy()
        for i in range(len(matrix) -2, -1, -1):
            for j in range(len(matrix[0])):
                cur = []
                if i + 1 < len(matrix) and j - 1 >= 0:
                    cur.append(matrix[i + 1][j - 1])
                if i + 1 < len(matrix) and j < len(matrix[0]):
                    cur.append(matrix[i + 1][j])
                if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
                    cur.append(matrix[i + 1][j + 1])
                dp[i][j] += min(cur)
        print(dp)
        return min(dp[0])

