
#1314
#medium

#Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

#i - k <= r <= i + k,
#j - k <= c <= j + k, and
#(r, c) is a valid position in the matrix.
 

#Example 1:

#Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
#Output: [[12,21,16],[27,45,33],[24,39,28]]
#Example 2:

#Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
#Output: [[45,45,45],[45,45,45],[45,45,45]]



#my own solution using python3:

#you don't have to iterate over the entire grid - just the rows - and do prefix sum of each row by cutting from right - left of prefix array

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        new = [[-1] * n for i in range(m)]
        pref = []
        for m in mat:
            pref.append(list(itertools.accumulate(m)))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(i, j)
                lowrow, lowcol = i - k, j - k 
                highrow, highcol = i + k, j + k 
                if lowrow < 0:
                    lowrow = 0
                if lowcol < 0:
                    lowcol = 0
                if highrow >= len(mat):
                    highrow = len(mat) - 1
                if highcol >= len(mat[0]):
                    highcol = len(mat[0]) - 1
                cursum = 0
                for a in range(lowrow, highrow + 1):
                    if lowcol <= 0:
                        cursum += pref[a][highcol]
                    else:
                        cursum += pref[a][highcol] - pref[a][lowcol - 1]
                print(cursum)
                new[i][j] = cursum



        return new
