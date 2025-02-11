#2012
#medium

#You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

#2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
#1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
#0, if none of the previous conditions holds.
#Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

 

#Example 1:

#Input: nums = [1,2,3]
#Output: 2
#Explanation: For each index i in the range 1 <= i <= 1:
#- The beauty of nums[1] equals 2.

#my own solution using python3:

#use a sorted list for the left and right sides

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res = 0
        lefts, rights = SortedList(), SortedList(nums)
        for i in range(len(nums)):
            rights.remove(nums[i])
            cur = nums[i]
            if i >= 1 and i < len(nums) - 1:
                if cur > lefts[-1] and cur < rights[0]:
                    res += 2
                elif nums[i - 1] < nums[i] < nums[i + 1]:
                    res += 1



            lefts.add(nums[i])
        return res
