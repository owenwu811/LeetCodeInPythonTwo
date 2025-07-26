#3191
#medium

#You are given a binary array nums.

#You can do the following operation on the array any number of times (possibly zero):

#Choose any 3 consecutive elements from the array and flip all of them.
#Flipping an element means changing its value from 0 to 1, and from 1 to 0.

#Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

#Example 1:

#Input: nums = [0,1,1,1,0,0]


#correct python3 solution (could not solve):

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                if nums[i + 1] == 0:
                    nums[i + 1] = 1
                elif nums[i + 1] == 1:
                    nums[i + 1] = 0
                if nums[i + 2] == 0:
                    nums[i + 2] = 1
                elif nums[i + 2] == 1:
                    nums[i + 2] = 0
               # nums[i + 2] = 1
                cnt += 1
        if nums[-1] == 0 or nums[-2] == 0: return -1
        return cnt
