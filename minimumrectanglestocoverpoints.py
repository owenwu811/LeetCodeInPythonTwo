
#3111
#medium

#You are given a 2D integer array points, where points[i] = [xi, yi]. You are also given an integer w. Your task is to cover all the given points with rectangles.

#Each rectangle has its lower end at some point (x1, 0) and its upper end at some point (x2, y2), where x1 <= x2, y2 >= 0, and the condition x2 - x1 <= w must be satisfied for each rectangle.

#A point is considered covered by a rectangle if it lies within or on the boundary of the rectangle.

#Return an integer denoting the minimum number of rectangles needed so that each point is covered by at least one rectangle.

#Note: A point may be covered by more than one rectangle.


#my own solution using python3:

#use a sorted list

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        res = 0
        tmp = SortedList()
        for p in points:
            if p[0] not in tmp:
                tmp.add(p[0])
        a = tmp
        print(a)
        i = 0
        ans = 0
        while i<len(a):
            ans+=1
            t=a[i]+w
            while i<len(a) and a[i]<=t:
                i+=1
        return ans
