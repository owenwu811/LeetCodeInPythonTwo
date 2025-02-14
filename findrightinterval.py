#436
#medium

#You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

#The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

#Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

#Example 1:

#Input: intervals = [[1,2]]
#Output: [-1]
#Explanation: There is only one interval in the collection, so it outputs -1.
#Example 2:

#Input: intervals = [[3,4],[2,3],[1,2]]
#Output: [-1,0,1]
#Explanation: There is no right interval for [3,4].
#The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
#The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
#Example 3:

#Input: intervals = [[1,4],[2,3],[3,4]]
#Output: [-1,2,-1]
#Explanation: There is no right interval for [1,4] and [3,4].
#The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.


#my own solution using python3:

#use a dictionary to keep track of {val: idx}, and then sort just the starts in an array so you can find the smallest element of the current end that's less than or equal to any start, and then get the index from the dictionary - if the current end is not, append -1

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        starts = SortedList()
        
        d = OrderedDict()
        for i, e in enumerate(intervals):
            starts.add(e[0])
            d[e[0]] = i
        #[3, 2, 1]
        #print(d)
        #print(starts)
        for i in range(len(intervals)):
            curend = intervals[i][1]
            b = bisect_left(starts, curend)
            #print(b, starts, curend)
            if b >= len(starts):
                res.append(-1)
            else:
                res.append(d[starts[b]])





        return res
        
