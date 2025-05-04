#120
#medium


#Given a triangle array, return the minimum path sum from top to bottom.

#For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

#Example 1:

#Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
#Output: 11
#Explanation: The triangle looks like:
#   2
#  3 4
# 6 5 7
#4 1 8 3
#The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
#Example 2:

#Input: triangle = [[-10]]
#Output: -10

#my own solution using python3:

#use top down tabulation

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle.copy()
         #[[2],
         #[3,4],
         #[6,5,7],
         #[4,1,8,3]]
        for i in range(len(triangle) -2, -1, -1):
            for j in range(i + 1):
                cur = []
                print(i + 1, j)
                print(i + 1, j + 1)
                cur.append(dp[i + 1][j])
                if j + 1 < len(dp):
                    cur.append(dp[i + 1][j + 1])
                print(dp[i][j], cur)
                dp[i][j] += min(cur)
        return dp[0][0]
