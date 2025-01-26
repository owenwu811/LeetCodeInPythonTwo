#2711
#medium


#Given a 2D grid of size m x n, you should find the matrix answer of size m x n.

#The cell answer[r][c] is calculated by looking at the diagonal values of the cell grid[r][c]:

#Let leftAbove[r][c] be the number of distinct values on the diagonal to the left and above the cell grid[r][c] not including the cell grid[r][c] itself.
#Let rightBelow[r][c] be the number of distinct values on the diagonal to the right and below the cell grid[r][c], not including the cell grid[r][c] itself.
#Then answer[r][c] = |leftAbove[r][c] - rightBelow[r][c]|.
#A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until the end of the matrix is reached.

#For example, in the below diagram the diagonal is highlighted using the cell with indices (2, 3) colored gray:
#Red-colored cells are left and above the cell.
#Blue-colored cells are right and below the cell.

#Input: grid = [[1,2,3],[3,1,5],[3,2,1]]

#Output: Output: [[1,1,0],[1,0,1],[0,1,1]]


#my own solution using python3:

#just brute force it by calculating the upper left and lower right diagonal set lengths and subtracting them for every cell in the grid

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        #[[1,2,3],
        #[3,1,5],
        #[3,2,1]]


        #[[1,1,0],
        #[1,0,1],
        #[0,1,1]]


        
        #0 0 set() {1}
        #0 1 set() {5}
        #0 2 set() set()
        #1 0 set() {2}
        #1 1 set() {1}
        #1 2 set() set()
        #2 0 set() set()
        #2 1 set() set()
        #2 2 {1} set()
        m, n = len(grid), len(grid[0])
        new = [[0] * n for i in range(m)]
        print(new)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                leftupx, leftupy = i - 1, j - 1
                belowrightx, belowrighty = i + 1, j + 1
                leftupset = set()
                belowrightset = set()
                while leftupx >= 0 and leftupy >= 0:
                    leftupset.add(grid[leftupx][leftupy])
                    leftupx -= 1
                    leftupy -= 1
                while belowrightx < len(grid) and belowrighty < len(grid[0]):
                    belowrightset.add(grid[belowrightx][belowrighty])
                    belowrightx += 1
                    belowrighty += 1
                #print(i, j, leftupset, belowrightset)
                if i == 1 and j == 1:
                    print(leftupset, belowrightset)
                diff = abs(len(leftupset) - len(belowrightset))
                print(i, j, "d", diff)
                new[i][j] = abs(len(leftupset) - len(belowrightset))
        return new
