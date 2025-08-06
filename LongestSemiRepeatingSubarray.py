#3641
#medium

#You are given an integer array nums of length n and an integer k.

#A semi‑repeating subarray is a contiguous subarray in which at most k elements repeat (i.e., appear more than once).

#Return the length of the longest semi‑repeating subarray in nums.

 

#Example 1:

#Input: nums = [1,2,3,1,2,3,4], k = 2

#Output: 6

#my own solution using python3:

#use sliding window to keep shrinking until k is met, and then take size of window

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        c = Counter()
        seen = set()
        for r in range(len(nums)):
            c[nums[r]] += 1
            if c[nums[r]] > 1:
                seen.add(nums[r])
            while len(seen) > k and l < r:
                c[nums[l]] -= 1
                if c[nums[l]] <= 1:
                    seen.discard(nums[l])
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
