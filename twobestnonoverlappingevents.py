#2054
#medium


#You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

#Return this maximum sum.

#Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

#Input: events = [[1,3,2],[4,5,2],[2,4,3]]
#Output: 4
#Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.



#my own solution using python3:

#we need to find the max element in a subarray, but you know the subarray is from current idx to end, so build a reverse array keeping track of the max element seen so far

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        res = 0
        events.sort(key=lambda x: (x[0], x[1], x[2]))
        starts = []
        other = []
        ends = []
        n = len(events)
        for i, e in enumerate(events):
            if e[2] >= res:
                res = e[2]
            starts.append(e[0])
            ends.append(e[1])
            other.append(e[2])
        #print(other)
        biggest = []
        bb = 0
        for o in other[::-1]:
            bb = max(bb, o)
            #print(bb)
            biggest.append(bb)
            #print(other, sl)
        print(other, biggest)
        for i in range(len(events)):
            s = bisect_right(starts, events[i][1])
            #print(s)
            if n - s >= 1:
                diff = n - s
                a = biggest[:diff]
                #print(other[s:], biggest[:diff])
                #print(other[s:], sl[:diff])
                res = max(res, events[i][2] + a[-1])
        return res
