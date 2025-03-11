
#487
#medium

#Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

#Example 1:

#Input: nums = [1,0,1,1,0]
#Output: 4
#Explanation: 
#- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
#- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
#The max number of consecutive ones is 4.


#could not solve

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        c = Counter()
        res = 0
        for r in range(len(nums)):
            c[nums[r]] += 1
            while c[0] > 1:
                c[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
