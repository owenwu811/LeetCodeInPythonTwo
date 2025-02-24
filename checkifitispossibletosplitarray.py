
#2811
#medium

#You are given an array nums of length n and an integer m. You need to determine if it is possible to split the array into n arrays of size 1 by performing a series of steps.

#An array is called good if:

#The length of the array is one, or
#The sum of the elements of the array is greater than or equal to m.
#In each step, you can select an existing array (which may be the result of previous steps) with a length of at least two and split it into two arrays, if both resulting arrays are good.

#Return true if you can split the given array into n arrays, otherwise return false.

 

#Example 1:

#Input: nums = [2, 2, 1], m = 4

#Output: true

#Explanation:

#Split [2, 2, 1] to [2, 2] and [1]. The array [1] has a length of one, and the array [2, 2] has the sum of its elements equal to 4 >= m, so both are good arrays.
#Split [2, 2] to [2] and [2]. both arrays have the length of one, so both are good arrays.




#correct python3 solution (could not solve):

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) < 3:
            return True
        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] >= m:
                return True
        return False
