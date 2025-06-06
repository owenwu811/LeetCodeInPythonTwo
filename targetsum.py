
#494
#medium

#You are given an integer array nums and an integer target.

#You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

#For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
#Return the number of different expressions that you can build, which evaluates to target.


#correct python3 solution (could not solve):

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtrack(i + 1, total + nums[i])) + (backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)
