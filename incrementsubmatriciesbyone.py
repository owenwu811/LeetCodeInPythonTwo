
#2536
#medium

#You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

#You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

#Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
#Return the matrix mat after performing every query.

#Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
#Output: [[1,1,0],[1,2,1],[0,1,1]]
#Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
#- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
#- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).


#my own solution using python3:

#use the difference array technique to increment every row's subarray by a fixed amount in 0(1)

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        print(res)
        for q in queries:
            rs, re = q[0], q[2]
            cs, ce = q[1], q[3]
            for i in range(rs, re + 1):
                res[i][cs] += 1
                if ce + 1 < len(res[i]):
                    res[i][ce + 1] -= 1
        print(res)

        #[[1, 0, -1], 
        #[1, 1, -1], 
        #[0, 1, 0]]

        ans = []
        for r in res:
            ans.append(list(itertools.accumulate(r)))
        return ans
