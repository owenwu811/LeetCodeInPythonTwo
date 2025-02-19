#3452
#easy

#Given an array of integers nums and an integer k, an element nums[i] is considered good if it is strictly greater than the elements at indices i - k and i + k (if those indices exist). If neither of these indices exists, nums[i] is still considered good.

#Return the sum of all the good elements in the array.

 

#Example 1:

#Input: nums = [1,3,2,1,5,4], k = 2

#Output: 12

#Explanation:

#The good numbers are nums[1] = 3, nums[4] = 5, and nums[5] = 4 because they are strictly greater than the numbers at indices i - k and i + k.



#my own solution using python3:

#very confusing description - really look at examples to understand

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            if i - k >= 0 and i + k < len(nums):
                behind = nums[i - k]
                after = nums[i + k]
                if behind < cur and after < cur:
                    print(i)
                    res += cur
            else:
                if i - k < 0 and i + k < len(nums) and cur > nums[i + k]:
                    
                    res += cur
                if i - k >= 0 and i + k >= len(nums) and cur > nums[i - k]:
                    res += cur
        return res
