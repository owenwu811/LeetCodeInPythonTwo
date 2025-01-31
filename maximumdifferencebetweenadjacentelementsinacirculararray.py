#3423
#easy

#Given a circular array nums, find the maximum absolute difference between adjacent elements.

#Note: In a circular array, the first and last elements are adjacent.

 

#Example 1:

#Input: nums = [1,2,4]

#Output: 3

#Explanation:

#Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.


#my own solution using python3:

#compare all adjacent elements as well as the 1st and last elements

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) - 1):
            res = max(res, abs(nums[i] - nums[i - 1]), abs(nums[i] - nums[i + 1]))
        res = max(res, abs(nums[0] - nums[-1]))
        return res
