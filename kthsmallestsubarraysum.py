#1918
#medium

#Given an integer array nums of length n and an integer k, return the kth smallest subarray sum.

#A subarray is defined as a non-empty contiguous sequence of elements in an array. A subarray sum is the sum of all elements in the subarray.

 

#Example 1:

#Input: nums = [2,1,3], k = 4
#Output: 3
#Explanation: The subarrays of [2,1,3] are:
#- [2] with sum 2
#- [1] with sum 1
#- [3] with sum 3
#- [2,1] with sum 3
#- [1,3] with sum 4
#- [2,1,3] with sum 6 
#Ordering the sums from smallest to largest gives 1, 2, 3, 3, 4, 6. The 4th smallest is 3.



#correct python3 solution (could not solve):

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def f(target):
            count = 0
            left = 0
            cursum = 0
            for right in range(len(nums)):
                cursum += nums[right]
                while cursum > target:
                    cursum -= nums[left]
                    left += 1
                count += right - left + 1
            return count
        left, right = min(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if f(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
