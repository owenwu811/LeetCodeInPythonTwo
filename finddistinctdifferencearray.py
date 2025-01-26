#2670
#easy


#You are given a 0-indexed array nums of length n.

#The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].

#Return the distinct difference array of nums.

#Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive. Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.

 

#Example 1:

#Input: nums = [1,2,3,4,5]
#Output: [-3,-1,1,3,5]
#Explanation: For index i = 0, there is 1 element in the prefix and 4 distinct elements in the suffix. Thus, diff[0] = 1 - 4 = -3.
#For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
#For index i = 2, there are 3 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 3 - 2 = 1.
#For index i = 3, there are 4 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 4 - 1 = 3.
#For index i = 4, there are 5 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 5 - 0 = 5.


#my own solution using python3:

#take the length of set up to and set right to end and subtract

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        #left, right = 0, len(nums)
        res = [0] * len(nums)
        for i in range(len(nums)):
            left = len(set(nums[:i + 1]))
            right = len(set(nums[i + 1:]))
            print(left, right, i)
            res[i] = left - right
        return res
