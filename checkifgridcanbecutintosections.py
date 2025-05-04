
#3394
#medium

#You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

#(startx, starty): The bottom-left corner of the rectangle.
#(endx, endy): The top-right corner of the rectangle.
#Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

#Each of the three resulting sections formed by the cuts contains at least one rectangle.
#Every rectangle belongs to exactly one section.
#Return true if such cuts can be made; otherwise, return false.

 

#Example 1:

#Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

#Output: true

#Explanation:



#my own solution using python3:

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
     
        xc = []
        yc = []
        for r in rectangles:
            #print(r[0], r[2])
            xc.append([r[0], r[2]])
            yc.append([r[1], r[3]])
        xc.sort()
        yc.sort()
        #print(xc)
        #print(yc)
        xx = [xc[0]]
        yy = [yc[0]]
        for i in range(1, len(xc)):
            if xc[i][0] < xx[-1][-1]:
                xx[-1][-1] = max(xx[-1][-1], xc[i][1])
            else:
                xx.append(xc[i])
        for i in range(1, len(yc)):
            if yc[i][0] < yy[-1][-1]:
                yy[-1][-1] = max(yy[-1][-1], yc[i][1])
            else:
                yy.append(yc[i])
        print(xx)
        print(yy)
        return len(xx) >= 3 or len(yy) >= 3
