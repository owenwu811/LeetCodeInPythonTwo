
#2778
#easy

#You are given a 1-indexed integer array nums of length n.

#An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

#Return the sum of the squares of all special elements of nums.

 

#Example 1:

#Input: nums = [1,2,3,4]
#Output: 21
#Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
#Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  


#my own solution using python3:

#be careful that they say 1 indexed, so you must do % (i + 1) instead of % i as normal

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            if n % (i + 1) == 0:
                res.append(cur)
        print(res)
        new = []
        for r in res:
            new.append(str(r))
            new.append("*")
            new.append(str(r))
            new.append("+")
        print(new)
        new.pop()
        return eval("".join(new))
