#2932
#easy

#You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

#|x - y| <= min(x, y)
#You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.

#Return the maximum XOR value out of all possible strong pairs in the array nums.

#Note that you can pick the same integer twice to form a pair.

 

#Example 1:

#Input: nums = [1,2,3,4,5]
#Output: 7
#Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
#The maximum XOR possible from these pairs is 3 XOR 4 = 7.


#my own solution using python3:

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)): 
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    cur = nums[i] ^ nums[j]
                    print(cur, nums[i], nums[j])
                    res = max(res, nums[i] ^ nums[j])
        return res
