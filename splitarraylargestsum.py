
#410
#hard

#Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

#Return the minimized largest sum of the split.

#A subarray is a contiguous part of the array.

 

#Example 1:

#Input: nums = [7,2,5,10,8], k = 2
#Output: 18
#Explanation: There are four ways to split nums into two subarrays.
#The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.


#correct python3 solution (could not solve) - just used my solution for capacity to ship packages within d days:

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        res = float('inf')
        weights = nums
        days = k
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            cap = mid
            cur = 0
            dt = 1
            for w in weights:
                if cur + w > cap:
                    dt += 1
                    cur = w
                else:
                    cur += w
            if dt <= days:
                res = min(res, cap)
                r = mid - 1
            else:
                l = mid + 1
        return res
