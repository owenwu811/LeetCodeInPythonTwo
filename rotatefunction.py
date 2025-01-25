#396
#medium

#You are given an integer array nums of length n.

#Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

##F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
#Return the maximum value of F(0), F(1), ..., F(n-1).

#The test cases are generated so that the answer fits in a 32-bit integer.


#correct python3 solution (could not solve without TLE):

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        totlength = len(nums)
        totsum = sum(nums)
        res = 0
        for i in range(len(nums)):
            res += (i * nums[i])
        now = res
        for i in range(len(nums) -1, -1, -1):
            cur = totsum - totlength * nums[i]
            now += cur
            res = max(res, now)
        return res
