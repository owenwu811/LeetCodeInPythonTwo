#3239
#medium

#You are given an m x n binary matrix grid.

#A row or column is considered palindromic if its values read the same forward and backward.

#You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

#Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.

#my own solution using python3:

#flip rows and then flip columns, and then get min of two

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows = 0
        orig = []
        for g in grid:
            nn = []
            for a in g:
                nn.append(a)
            orig.append(nn.copy())
                
        for g in grid:
            if g != g[::-1]:
                #print(g)
                l, r = 0, len(g) - 1
                while l < r:
                    if g[l] != g[r]:
                        g[r] = g[l]
                        rows += 1
                    l += 1
                    r -= 1
                #print(now)
        #print(rows)
        cols = []
        i = 0
        while i < len(orig[0]):
            cur = []
            for j in range(len(orig)):
                #print(j, i)
                cur.append(orig[j][i])
            cols.append(cur.copy())

            i += 1
        #[[1,0,0],
        #[0,0,0],
        #[0,0,1]]
        #print(cols)
        columncnt = 0
        for c in cols:
            if c != c[::-1]:
                l, r = 0, len(c) - 1
                while l < r:
                    if c[l] != c[r]:
                        columncnt += 1
                    l += 1
                    r -= 1
        return min(columncnt, rows)

