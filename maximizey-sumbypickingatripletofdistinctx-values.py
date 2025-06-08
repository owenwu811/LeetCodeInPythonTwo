#3572
#medium

#You are given two integer arrays x and y, each of length n. You must choose three distinct indices i, j, and k such that:

#x[i] != x[j]
#x[j] != x[k]
#x[k] != x[i]
#Your goal is to maximize the value of y[i] + y[j] + y[k] under these conditions. Return the maximum possible sum that can be obtained by choosing such a triplet of indices.

#If no such triplet exists, return -1.

 

#Example 1:

#Input: x = [1,2,1,3,2], y = [5,3,4,6,2]

#Output: 14

#my own solution using python3:

#my idea is to map the x value to the same index y value, and then sort by the biggest y value aka -1 of the sorted list

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        d = defaultdict(SortedList)
        for i, v in enumerate(x):
            d[v].add(y[i])
        #print(d)
        dd = defaultdict(SortedList)
        for a, b in d.items():
            for k in b:
                dd[k].add(a)
        #print(dd)
        aa = list(d.items())
        aa.sort(key=lambda x: x[1][-1])
        #print(aa)
        if len(aa) < 3:
            return -1
        print(aa[-4:])
        first = aa[-1][-1][-1]
        second = aa[-2][-1][-1]
        third = aa[-3][-1][-1]
        print(first, second, third)
        return first + second + third
