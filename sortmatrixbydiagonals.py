
#3446
#medium

#You are given an n x n square matrix of integers grid. Return the matrix such that:

#The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
#The diagonals in the top-right triangle are sorted in non-decreasing order.
 

#Example 1:

#Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

#Output: [[8,2,3],[9,6,7],[4,5,1]]



#my own solution using python3:

#just do brute force

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        #[[1,7,3],
        #[9,8,2],
        #[4,5,6]]
        
        
        startx, starty = len(grid), 0
        while startx > 0:
            startx -= 1
            #print(startx, starty)
            currow = []
            curx, cury = startx, starty
            while curx < len(grid) and cury < len(grid[0]):
                #print(curx, cury, "curx, cury")
                currow.append(grid[curx][cury])
                curx += 1
                cury += 1
                #print(curx, cury)
            currow.sort(reverse=True)
            c = deque(currow)
            print(c)
            nowx, nowy = startx, starty
            print(nowx, nowy)
            while nowx < len(grid) and nowy < len(grid[0]):
                if not c:
                    break
                print(nowx, nowy, c[0])
                grid[nowx][nowy] = c.popleft()
                nowx += 1
                nowy += 1
            print(grid)
                
        startx, starty = 0, 0
        while starty < len(grid[0]):
            starty += 1
            #print(startx, starty)
            curx, cury = startx, starty
            currow = []
            while curx < len(grid) and cury < len(grid[0]):
                #print(curx, cury, "curx2, cury2")
                
                currow.append(grid[curx][cury])
                curx += 1
                cury += 1
            currow.sort()
            c = deque(currow)
            print(c)
            nowx, nowy = startx, starty
            while nowx < len(grid) and nowy < len(grid[0]):
                if not c:
                    break
                print(nowx, nowy, c[0])
                grid[nowx][nowy] = c.popleft()
                nowx += 1
                nowy += 1
            print(grid)
        #print(grid)

                
        res = []
        for g in grid:
            res.append(g)
        return res
        #[[8,2,3],
        #[9,6,7],
        #[4,5,1]]
            
