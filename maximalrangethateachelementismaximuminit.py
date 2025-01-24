
#2832
#medium

#You are given a 0-indexed array nums of distinct integers.

#Let us define a 0-indexed array ans of the same length as nums in the following way:

#ans[i] is the maximum length of a subarray nums[l..r], such that the maximum element in that subarray is equal to nums[i].
#Return the array ans.

#Note that a subarray is a contiguous part of the array.

 

#Example 1:

#Input: nums = [1,5,4,3,6]
#Output: [1,4,2,1,5]
#Explanation: For nums[0] the longest subarray in which 1 is the maximum is nums[0..0] so ans[0] = 1.
#For nums[1] the longest subarray in which 5 is the maximum is nums[0..3] so ans[1] = 4.
#For nums[2] the longest subarray in which 4 is the maximum is nums[2..3] so ans[2] = 2.
#For nums[3] the longest subarray in which 3 is the maximum is nums[3..3] so ans[3] = 1.
#For nums[4] the longest subarray in which 6 is the maximum is nums[0..4] so ans[4] = 5.

#correct python3 solution (could not solve):

class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        stack = []
        nums.append(float('inf'))
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                index = stack.pop()
                nums[index] = i - stack[-1] -1 if stack else i
            stack.append(i)
        return nums[:-1]
