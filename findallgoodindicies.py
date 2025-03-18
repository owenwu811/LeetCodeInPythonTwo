#2420
#medium

#You are given a 0-indexed integer array nums of size n and a positive integer k.

#We call an index i in the range k <= i < n - k good if the following conditions are satisfied:

#The k elements that are just before the index i are in non-increasing order.
#The k elements that are just after the index i are in non-decreasing order.
#Return an array of all good indices sorted in increasing order.

 

#Example 1:

#Input: nums = [2,1,1,1,3,4,1], k = 2
#Output: [2,3]
#Explanation: There are two good indices in the array:
#- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
#- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
#Note that the index 4 is not good because [4,1] is not non-decreasing.


#correct python3 solution (could not solve):

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(len(nums) -2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1
        res = []
        for i in range(k, len(nums) - k):
            if left[i - 1] >= k and right[i + 1] >= k:
                res.append(i)
        return res
