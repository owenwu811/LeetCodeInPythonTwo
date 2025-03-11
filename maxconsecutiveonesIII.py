#1004
#medium

#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

#Example 1:

#Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#Output: 6
#Explanation: [1,1,1,0,0,1,1,1,1,1,1]
#Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

#my own solution using python3 after looking up number 2 of the same question:

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        c = Counter()
        res = 0
        for r in range(len(nums)):
            c[nums[r]] += 1
            while c[0] > k:
                c[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
