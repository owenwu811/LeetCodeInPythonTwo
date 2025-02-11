
#2874
#medium

#You are given a 0-indexed integer array nums.

#Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

#The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

 

#Example 1:

#Input: nums = [12,6,1,2,7]
#Output: 77
#Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
#It can be shown that there are no ordered triplets of indices with a value greater than 77. 
#Example 2:

#Input: nums = [1,10,3,4,19]
#Output: 133
#Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
#It can be shown that there are no ordered triplets of indices with a value greater than 133.

#my own solution using python3:

#use a sorted list to isolate the left, current element, and right sides, and try to maximize the value since you know the elements are already sorted, and you also know you have to include the current element in the triplet sum calulcation

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        lefts, rights = SortedList(), SortedList(nums)
        res = 0
        for i in range(len(nums)):
            rights.remove(nums[i])
            cur = nums[i]
            if i >= 1 and i < len(nums) - 1:

                target = lefts[-1]
                res = max(res, (target - cur) * rights[-1])



            lefts.add(nums[i])
        return res
