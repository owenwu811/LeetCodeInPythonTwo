#2655
#medium

#You are given an integer n which is the length of a 0-indexed array nums, and a 0-indexed 2D-array ranges, which is a list of sub-ranges of nums (sub-ranges may overlap).

#Each row ranges[i] has exactly 2 cells:

#ranges[i][0], which shows the start of the ith range (inclusive)
#ranges[i][1], which shows the end of the ith range (inclusive)
#These ranges cover some cells of nums and leave some cells uncovered. Your task is to find all of the uncovered ranges with maximal length.

#Return a 2D-array answer of the uncovered ranges, sorted by the starting point in ascending order.

#By all of the uncovered ranges with maximal length, we mean satisfying two conditions:

#Each uncovered cell should belong to exactly one sub-range
#There should not exist two ranges (l1, r1) and (l2, r2) such that r1 + 1 = l2

#Input: n = 10, ranges = [[3,5],[7,8]]
#Output: [[0,2],[6,6],[9,9]]


#my own solution using python3:

#merge the intervals first, and then keep track of before and after of each range - takes a bit of trial and error

class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        ranges.sort()
        if ranges:
            new = [ranges[0]]
            smallest = 0
            largest = n - 1
            edges = [smallest, largest]
            if new[0][0] <= smallest <= new[-1][-1]:
                edges.remove(smallest)
            if new[0][0] <= largest <= new[-1][-1]:
                edges.remove(largest)
            for i in range(1, len(ranges)):
                if ranges[i][0] <= smallest <= ranges[i][1] and smallest in edges:
                    edges.remove(smallest)
                if ranges[i][0] <= largest <= ranges[i][1] and largest in edges:
                    edges.remove(largest)
                if ranges[i][0] <= new[-1][-1] + 1:
                    new[-1][-1] = max(new[-1][-1], ranges[i][1])
                else:
                    new.append(ranges[i])
            print(new)
            sl = SortedList()
            for cur in new:
                low = cur[0] - 1
                high = cur[1] + 1
                if low >= 0:
                    sl.add(low)
                if high < n:
                    sl.add(high)
            print(edges, sl)

            for e in edges:
                sl.add(e)
            res = []
            for i in range(1, len(sl), 2):
                res.append([sl[i - 1], sl[i]])
            return res
        ans = [0, n - 1]
        return [ans]
