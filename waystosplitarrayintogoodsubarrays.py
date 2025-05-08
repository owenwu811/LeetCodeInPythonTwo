#2750
#medium

#You are given a binary array nums.

#A subarray of an array is good if it contains exactly one element with the value 1.

#Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [0,1,0,0,1]
#Output: 3
#Explanation: There are 3 ways to split nums into good subarrays:
#- [0,1] [0,0,1]
#- [0,1,0] [0,1]
#- [0,1,0,0] [1]


#my own solution using python3 after reading hint:

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        ones = []
        mod = ((10 ** 9) + 7)
        if 1 not in nums:
            return 0
        for i, n in enumerate(nums):
            if n == 1:
                ones.append(i)
        print(ones)
        ans = 1
        for i in range(1, len(ones)):
            ans *= (ones[i] - ones[i - 1])
        return ans % mod
