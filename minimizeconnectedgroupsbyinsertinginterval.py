
#3323
#medium

#You are given a 2D array intervals, where intervals[i] = [starti, endi] represents the start and the end of interval i. You are also given an integer k.

#You must add exactly one new interval [startnew, endnew] to the array such that:

#The length of the new interval, endnew - startnew, is at most k.
#After adding, the number of connected groups in intervals is minimized.
#A connected group of intervals is a maximal collection of intervals that, when considered together, cover a continuous range from the smallest point to the largest point with no gaps between them. Here are some examples:

#A group of intervals [[1, 2], [2, 5], [3, 3]] is connected because together they cover the range from 1 to 5 without any gaps.
#However, a group of intervals [[1, 2], [3, 4]] is not connected because the segment (2, 3) is not covered.
#Return the minimum number of connected groups after adding exactly one new interval to the array.

 

#Example 1:

#Input: intervals = [[1,3],[5,6],[8,10]], k = 3

#Output: 2

#my own solution using python3:

#for each jump, use binary search to see how far you can cover, and find the max number of elements you can cover, and subtract from the total

class Solution:
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:
        intervals.sort()
        #print(intervals)
        #[[1, 3], [5, 6], [8, 10]]
        #[[1, 1], [3, 3], [5, 10]]
        starts = []
        ends = []
        new = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new[-1][-1]:
                new[-1][-1] = max(new[-1][-1], intervals[i][1])
            else:
                new.append(intervals[i])
        print(new)
        for n in new:
            starts.append(n[0])
            ends.append(n[1])
        print(starts, ends)
        myset = set()
        ans = 0
        for i, n in enumerate(new):
            jump = n[1] + k
            b = bisect_right(starts, jump)
            #print(i, b - 1)
            diff = b - 1 - i
            print(diff)
            ans = max(ans, diff)
            myset.add(b)
        return len(new) - ans
