#304
#medium

#Given a 2D matrix matrix, handle multiple queries of the following type:

#Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#Implement the NumMatrix class:

#NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
#int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#You must design an algorithm where sumRegion works on O(1) time complexity.

#Input
#["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
#[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
#Output
#[null, 8, 11, 12]

#my own solution using python3:

#instead of building a grid, we can still iterate over each row, so just accumulate each row and use prefix sums

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.new = []
        for m in matrix:
            self.new.append(list(itertools.accumulate(m)))
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            high = col2
            low = col1
            if low <= 0:
                res += self.new[i][high]
            else:
                res += self.new[i][high] - self.new[i][low - 1]

        return res
