#2470
#medium

#Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

#A subarray is a contiguous non-empty sequence of elements within an array.

#The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

 

#Example 1:

#Input: nums = [3,6,2,7,1], k = 6
#Output: 4
#Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
#- [3,6,2,7,1]
#- [3,6,2,7,1]
#- [3,6,2,7,1]
#- [3,6,2,7,1]

#my own solution using python3:

#very easy double loop approach

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            #cur = [i]
            a = nums[i]
            for j in range(i, len(nums)):
                a = lcm(a, nums[j])
                if a == k:
                    res += 1
        return res
