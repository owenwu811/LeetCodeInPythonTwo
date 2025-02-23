#3462
#medium

#You are given a 2D integer matrix grid of size n x m, an integer array limits of length n, and an integer k. The task is to find the maximum sum of at most k elements from the matrix grid such that:

#The number of elements taken from the ith row of grid does not exceed limits[i].

#Return the maximum sum.

 

#Example 1:

#Input: grid = [[1,2],[3,4]], limits = [1,2], k = 2

#Output: 7

#Explanation:

#From the second row, we can take at most 2 elements. The elements taken are 4 and 3.
#The maximum possible sum of at most 2 selected elements is 4 + 3 = 7.


#my own solution using python3:

#take the k biggest elements based on limit from each row, and sum them up at the end

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if k == 0:
            return 0
        res = []
        for i, g in enumerate(grid):
            curlim = limits[i]
            s = SortedList(g)
            now = s[::-1]
            lim = now[:curlim]
            res.extend(lim)
        res.sort()
        return sum(res[-k:])
