#3427
#easy

#You are given an integer array nums of size n. For each index i where 0 <= i < n, define a 
#subarray
# nums[start ... i] where start = max(0, i - nums[i]).

#Return the total sum of all elements from the subarray defined for each index in the array.

 

#Example 1:

#Input: nums = [2,3,1]



#my own solution using python3:

#simple follow the instructions

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            subarraystart = max(0, i - nums[i])
            subarrend = i
            res += sum(nums[subarraystart: subarrend + 1])
        return res
