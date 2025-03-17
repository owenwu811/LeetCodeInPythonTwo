#2447
#medium


#Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

#A subarray is a contiguous non-empty sequence of elements within an array.

#The greatest common divisor of an array is the largest integer that evenly divides all the array elements.

 

#Example 1:

#Input: nums = [9,3,1,2,6,3], k = 3
#Output: 4
#Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
#- [9,3,1,2,6,3]
#- [9,3,1,2,6,3]
#- [9,3,1,2,6,3]
#- [9,3,1,2,6,3]


#my own solution using python3:

#just use double loop

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = gcd(cur, nums[j])
                if cur == k:
                    res += 1
        return res
                
