#2364
#medium

#You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

#Return the total number of bad pairs in nums.



#another question where you memorize tricks and it's inuitive (could not solve "fast enough"):

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c = Counter()
        res = 0
        for i, n in enumerate(nums):
            res += (i - c[n - i])
            c[n - i] += 1
        return res
