
#3467
#easy

#You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

#Replace each even number with 0.
#Replace each odd numbers with 1.
#Sort the modified array in non-decreasing order.
#Return the resulting array after performing these operations.

 

#Example 1:

#Input: nums = [4,3,2,1]

#Output: [0,0,1,1]

#Explanation:

#Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
#After sorting nums in non-descending order, nums = [0, 0, 1, 1].

#my own solution using python3:

#just follow the instructions

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            if n % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        nums.sort()
        return nums
