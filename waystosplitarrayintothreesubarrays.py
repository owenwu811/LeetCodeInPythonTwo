#1712
#medium

#A split of an integer array is good if:

#The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
#The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
#Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

#Example 1:

#Input: nums = [1,1,1]
#Output: 1
#Explanation: The only good way to split nums is [1] [1] [1].

#my own solution using python3:

#use binary search over the right two halves

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        p = list(itertools.accumulate(nums))
        tot = p[-1]
        mod = ((10 ** 9) + 7)
        ans = 0
        now = p.copy()
        for i in range(len(nums)):
            cur = p[i]
            del now[0]
            bl = bisect_left(now, cur * 2) 
            #if now:
            l, r = bl, len(now) - 1
            rr = float('-inf')
            while l < r:
                mid = (l + r) // 2
                if cur <= now[mid] - cur <= tot - now[mid]:
                    rr = max(rr, mid - bl + 1)
                    l = mid + 1
                else:
                    r = mid 
            if rr != float('-inf'):
                ans += rr
        return ans % mod
