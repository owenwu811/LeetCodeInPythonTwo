#1546
#medium

#Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

 

#Example 1:

#Input: nums = [1,1,1,1,1], target = 2
#Output: 2
#Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
#Example 2:

#Input: nums = [-1,3,5,1,4,2,-9], target = 6
#Output: 2
#Explanation: There are 3 subarrays with sum equal to 6.
#([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.



#correct python3 solution (could not solve):

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cursum = 0
        res = 0
        d = defaultdict(int)
        d[0] = 1
        for i, n in enumerate(nums):
            cursum += n
            if d[cursum - target] > 0:
                res += 1
                d.clear()
                cursum = 0
            d[cursum] += 1
        return res
