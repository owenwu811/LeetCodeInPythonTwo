
#867
#easy

#Given a 2D integer array matrix, return the transpose of matrix.

#The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[1,4,7],[2,5,8],[3,6,9]]


#my own solution using python3:

#you just get each column and put it in as rows and return the result

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(matrix[0]):
            cur = []
            for j in range(len(matrix)):
                print(j, i)
                cur.append(matrix[j][i])
            i += 1
            res.append(cur)
        return res
