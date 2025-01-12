#1746
#medium

#You are given an integer array nums. You must perform exactly one operation where you can replace one element nums[i] with nums[i] * nums[i]. 

#Return the maximum possible subarray sum after exactly one operation. The subarray must be non-empty.

 

#Example 1:

#Input: nums = [2,-1,-4,-3]
#Output: 17
#Explanation: You can perform the operation on index 2 (0-indexed) to make nums = [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17.

#my own solution using python3:

#use Kadane's algorithm to keep track of different states

class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        ans = max(nums[0], nums[0] ** 2)
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)):
            start = max(start + nums[i], end + nums[i] ** 2, nums[i] ** 2)
            end = max(nums[i], end + nums[i])
            ans = max(ans, start, end)
        return ans
