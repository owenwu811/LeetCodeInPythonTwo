#289
#medium


#According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

#The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

#Any live cell with fewer than two live neighbors dies as if caused by under-population.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by over-population.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

#Given the current state of the board, update the board to reflect its next state.

#Note that you do not need to return anything.


#my own solution using python3:

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #live = 1, dead = 0
        #exactly 3 1 valued neighbors means 0 becomes 1
        #1 cell with < 2 live neighbors becomes 0
        new = board.copy() 
        another = []
        for n in board:
            another.append(n.copy())
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    liveneic, deadneic = 0, 0
                    upx, upy = i - 1, j
                    if upx >= 0 and upx < len(board) and upy >= 0 and upy < len(board[0]):
                        if board[upx][upy] == 0:
                            deadneic += 1
                        elif board[upx][upy] == 1:
                            liveneic += 1
                    downx, downy = i + 1, j
                    if downx >= 0 and downx < len(board) and downy >= 0 and downy < len(board[0]):
                        if board[downx][downy] == 0:
                            deadneic += 1
                        elif board[downx][downy] == 1:
                            liveneic += 1
                    rightx, righty = i, j + 1
                    if rightx >= 0 and rightx < len(board) and righty >= 0 and righty < len(board[0]):
                        if board[rightx][righty] == 0:
                            deadneic += 1
                        elif board[rightx][righty] == 1:
                            liveneic += 1
                    leftx, lefty = i, j - 1
                    if leftx >= 0 and leftx < len(board) and lefty >= 0 and lefty < len(board[0]):
                        if board[leftx][lefty] == 0:
                            deadneic += 1
                        elif board[leftx][lefty] == 1:
                            liveneic += 1
                    uprightx, uprighty = i - 1, j + 1
                    if uprightx >= 0 and uprightx < len(board) and uprighty >= 0 and uprighty < len(board[0]):
                        if board[uprightx][uprighty] == 0:
                            deadneic += 1
                        elif board[uprightx][uprighty] == 1:
                            liveneic += 1
                    upleftx, uplefty = i - 1, j - 1
                    if upleftx >= 0 and upleftx < len(board) and uplefty >= 0 and uplefty < len(board[0]):
                        if board[upleftx][uplefty] == 0:
                            deadneic += 1
                        elif board[upleftx][uplefty] == 1:
                            liveneic += 1
                    downleftx, downlefty = i + 1, j - 1
                    if downleftx >= 0 and downleftx < len(board) and downlefty >= 0 and downlefty < len(board[0]):
                        if board[downleftx][downlefty] == 0:
                            deadneic += 1
                        elif board[downleftx][downlefty] == 1:
                            liveneic += 1
                    downrightx, downrighty = i + 1, j + 1
                    if downrightx >= 0 and downrightx < len(board) and downrighty >= 0 and downrighty < len(board[0]):
                        if board[downrightx][downrighty] == 0:
                            deadneic += 1
                        elif board[downrightx][downrighty] == 1:
                            liveneic += 1
                elif board[i][j] == 0: # so if exactly 3 1 neighbors, set to 1
                    liveneic, deadneic = 0, 0
                    upx, upy = i - 1, j
                    if upx >= 0 and upx < len(board) and upy >= 0 and upy < len(board[0]):
                        if board[upx][upy] == 0:
                            deadneic += 1
                        elif board[upx][upy] == 1:
                            liveneic += 1
                    downx, downy = i + 1, j
                    if downx >= 0 and downx < len(board) and downy >= 0 and downy < len(board[0]):
                        if board[downx][downy] == 0:
                            deadneic += 1
                        elif board[downx][downy] == 1:
                            liveneic += 1
                    rightx, righty = i, j + 1
                    if rightx >= 0 and rightx < len(board) and righty >= 0 and righty < len(board[0]):
                        if board[rightx][righty] == 0:
                            deadneic += 1
                        elif board[rightx][righty] == 1:
                            liveneic += 1
                    leftx, lefty = i, j - 1
                    if leftx >= 0 and leftx < len(board) and lefty >= 0 and lefty < len(board[0]):
                        if board[leftx][lefty] == 0:
                            deadneic += 1
                        elif board[leftx][lefty] == 1:
                            liveneic += 1
                    uprightx, uprighty = i - 1, j + 1
                    if uprightx >= 0 and uprightx < len(board) and uprighty >= 0 and uprighty < len(board[0]):
                        if board[uprightx][uprighty] == 0:
                            deadneic += 1
                        elif board[uprightx][uprighty] == 1:
                            liveneic += 1
                    upleftx, uplefty = i - 1, j - 1
                    if upleftx >= 0 and upleftx < len(board) and uplefty >= 0 and uplefty < len(board[0]):
                        if board[upleftx][uplefty] == 0:
                            deadneic += 1
                        elif board[upleftx][uplefty] == 1:
                            liveneic += 1
                    downleftx, downlefty = i + 1, j - 1
                    if downleftx >= 0 and downleftx < len(board) and downlefty >= 0 and downlefty < len(board[0]):
                        if board[downleftx][downlefty] == 0:
                            deadneic += 1
                        elif board[downleftx][downlefty] == 1:
                            liveneic += 1
                    downrightx, downrighty = i + 1, j + 1
                    if downrightx >= 0 and downrightx < len(board) and downrighty >= 0 and downrighty < len(board[0]):
                        if board[downrightx][downrighty] == 0:
                            deadneic += 1
                        elif board[downrightx][downrighty] == 1:
                            liveneic += 1
                print("dead", deadneic, "live", liveneic,  "i", i, "j", j, board[i][j])

                if board[i][j] == 0:
                    if liveneic == 3:
                        print(board, "b")
                        another[i][j] = 1
                        print(another, "a")
                        print(board, "b")
                elif board[i][j] == 1:
                    if liveneic < 2:
                        another[i][j] = 0
                    if liveneic > 3:
                        another[i][j] = 0
        print(another)
        board[:] = another
      

