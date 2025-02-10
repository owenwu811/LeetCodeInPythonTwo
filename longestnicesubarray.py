
#2401
#medium

#You are given an array nums consisting of positive integers.

#We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

#Return the length of the longest nice subarray.

#A subarray is a contiguous part of an array.

#Note that subarrays of length 1 are always considered nice.


#correct python3 solution (could not solve):

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        l = 0
        for r in range(len(nums)):
            while cur & nums[r] > 0:
                cur = cur ^ nums[l]
                l += 1
            cur = cur | nums[r]
            print(r, l)
            res = max(res, r - l + 1)
        return res



#2/9/25 review (could not solve):

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        cur = 0
        res = 0
        for r in range(len(nums)):
            while cur & nums[r]:
                cur = cur ^ nums[l]
                l += 1
            cur = cur | nums[r]
            res = max(res, r - l + 1)
        return res
