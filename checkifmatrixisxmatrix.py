


#2319
#easy

#A square matrix is said to be an X-Matrix if both of the following conditions hold:

#All the elements in the diagonals of the matrix are non-zero.
#All other elements are 0.
#Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.

#my own solution using python3:

#be careful of edge cases 

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        if grid[-1][1] != 0:
            return False
        totzeros = 0
        nonzeroes = 0
        for g in grid:
            totzeros += g.count(0)
            nonzeroes += (len(g) - g.count(0))
        print(totzeros)
        print(nonzeroes)
        posx, posy = 0, 0
        while posx < len(grid) and posy < len(grid[0]):
            if grid[posx][posy] != 0:
                nonzeroes -= 1
            else:
                return False
            posx += 1
            posy += 1
        print(nonzeroes)
        negx, negy = len(grid[0]) - 1, 0
        print(negx, negy)
        while negx >= 0 and negx < len(grid) and negy >= 0 and negy < len(grid[0]):
            print(negx, negy)
            if grid[negx][negy] != 0:
                nonzeroes -= 1
            else:
                return False
            negx -= 1
            negy += 1
            print(negx, negy)
        for i in range(1, len(grid) - 1):
            if grid[i][-1] != 0 or grid[i][0] != 0:
                return False
        
        #[[6,0,19],
        #[0,2,0],
        #[13,17,6]]
        return nonzeroes <= 0 
        #[0, 3] > [1, 2] > [2, 1] > [3, 0]
        #[[2,0,0,0,1],
        #[0,4,0,1,5],
        #[0,0,5,0,0],
        #[0,5,0,2,0],
        #[4,0,0,0,2]]
