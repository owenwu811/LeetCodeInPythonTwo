#3550
#easy

#You are given an integer array nums.

#Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

#If no such index exists, return -1.

 

#Example 1:

#Input: nums = [1,3,2]

#Output: 2

#Explanation:

#For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.


#My own solution using python3:

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            cur = 0

            for j in str(n):
                cur += int(j)
            if i == cur:
                return i
        return -1
