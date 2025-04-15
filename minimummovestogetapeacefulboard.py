
#3189
#medium

#Given a 2D array rooks of length n, where rooks[i] = [xi, yi] indicates the position of a rook on an n x n chess board. Your task is to move the rooks 1 cell at a time vertically or horizontally (to an adjacent cell) such that the board becomes peaceful.

#A board is peaceful if there is exactly one rook in each row and each column.

#Return the minimum number of moves required to get a peaceful board.

#Note that at no point can there be two rooks in the same cell.

 

#Example 1:

#Input: rooks = [[0,0],[1,0],[1,1]]

#Output: 3


#my own solution using python3 after reading hints:

#sort by rows and then columns

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        rooks.sort()
        print(rooks)
        ans = 0
        for i, r in enumerate(rooks):
            diff = abs(i - r[0])
            ans += diff

        rooks.sort(key=lambda x: x[1])
        print(rooks)
        for i, r in enumerate(rooks):
            diff = abs(i - r[1])
            ans += diff

        return ans
