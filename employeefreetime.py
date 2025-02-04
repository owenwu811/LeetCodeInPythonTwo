
#759
#hard

#We are given a list schedule of employees, which represents the working time for each employee.

#Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

#Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

#(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

#Example 1:

#Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
#Output: [[3,4]]
#Explanation: There are a total of three employees, and all common
#free time intervals would be [-inf, 1], [3, 4], [10, inf].
#We discard any intervals that contain inf as they aren't finite.
#Example 2:

#Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
#Output: [[5,6],[7,9]]


#my own solution using python3:

#sort the intervals and take the non overlapping ones based on the 1st index's largest historical value

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        res = []
        for s in schedule:
            for a in s:
                #print(a.start, a.end)
                res.append([a.start, a.end])
        res.sort()
        print(res)
        #[[0, 25], [5, 16], [6, 24], [7, 24], [9, 16], [18, 26], [27, 35], [29, 31], [29, 33], [33, 36], [39, 57], [40, 47], [40, 55], [43, 49], [45, 57], [56, 59], [57, 87], [61, 75], [65, 74], [66, 69], [68, 71], [78, 81], [80, 81], [91, 94], [94, 99]]
        #[[16,18],[26,27],[36,39],[71,78],[81,91]]
        #[[26,27],[36,39],[87,91]]
        ans = []
        biggesty = res[0][1]
        biggestx = res[0][0]
        for i in range(1, len(res)):
            if res[i][0] > biggesty:
                print(biggesty, res[i - 1][1], res[i][0])
                ans.append(Interval(max(biggesty, res[i - 1][1]), res[i][0]))
            biggestx = max(biggestx, res[i][0])
            biggesty = max(biggesty, res[i][1])
        return ans
