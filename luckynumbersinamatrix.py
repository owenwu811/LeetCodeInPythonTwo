#1380
#easy

#Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

#A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

#Example 1:

#Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
#Output: [15]
#Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
#Example 2:

#Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
#Output: [12]
#Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
#Example 3:

#Input: matrix = [[7,8],[1,2]]
#Output: [7]
#Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.


#my own solution using python3:

#get all rows and columns and compare as stated for each row and column - make sure to not have index out of bounds errors by adjusting the dimensions of the grid

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = []
        for m in matrix:
            rows.append(m)
        cols = []
        h = 0
        while h < len(matrix[0]):
            curcol = []
            for j in range(len(matrix)):
                #print(j, h)
                curcol.append(matrix[j][h])
            cols.append(curcol)
            h += 1
        res = []
        print(rows, cols)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                cur = matrix[i][j]
                if cur == 15:
                    print(rows[i], cols[j], i, j, cur)
                if cur == min(rows[i]) and cur == max(cols[j]):
                    print(cur)
                    res.append(cur)
        return res
