
#3520
#medium

#You are given an array of integers nums and an integer k.

#An inversion pair with a threshold x is defined as a pair of indices (i, j) such that:

#i < j
#nums[i] > nums[j]
#The difference between the two numbers is at most x (i.e. nums[i] - nums[j] <= x).
#Your task is to determine the minimum integer min_threshold such that there are at least k inversion pairs with threshold min_threshold.

#If no such integer exists, return -1.

 

#Example 1:

#Input: nums = [1,2,3,4,3,2,1], k = 7

#Output: 2


#my own solution using python3:

#use binary search and then find all numbers greater than nums[i] to the right of nums[i], and then the range of mid + and mid - nums[i]

class Solution:
    def minThreshold(self, nums: List[int], k: int) -> int:
        l, r = 0, max(nums)
        res = float('inf')
        sl = SortedList(nums)
        d = dict()
        new = sl.copy()
        for i in range(len(nums)):
            new.discard(nums[i])
            bll = bisect_left(new, nums[i])
            d[i] = new[:bll]

        while l <= r:
            mid = (l + r) // 2
            ans = 0
            now = sl.copy()
            for i in range(len(nums)):
                now.discard(nums[i])
                bl = bisect_left(now, nums[i])
                if nums[i] - mid <= nums[i] + mid:
                    low = nums[i] - mid
                    high = nums[i] + mid
                else:
                    low = nums[i] + mid
                    high = nums[i] - mid
                ll = bisect_left(d[i], low)
                rr = bisect_left(d[i], high)
                ans += (rr - ll)
            if ans >= k:
                if mid <= res:
                    res = mid
                r = mid - 1
            else: l = mid + 1
        if res == float('inf'):
            return -1
        return res
        
