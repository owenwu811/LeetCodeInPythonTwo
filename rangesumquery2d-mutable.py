#308
#medium

#Given a 2D matrix matrix, handle multiple queries of the following types:

#Update the value of a cell in matrix.
#Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#Implement the NumMatrix class:

#NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
#void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
#int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).



#my own solution using python3:

#very simple - just follow the instructions and loop from the top left corner to bottom right corner and add each cell's value and return the total

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix

    def update(self, row: int, col: int, val: int) -> None:
        self.mat[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                res += self.mat[i][j]
        return res


#another easy solution of mine to change it up:

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix

    def update(self, row: int, col: int, val: int) -> None:
        self.mat[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        rows = []
        for i in range(row1, row2 + 1):
            rows.append(self.mat[i])

        for r in rows:
            new = r[col1: col2 + 1]
            res += sum(new)
        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
