
#2501
#medium

#You are given an integer array nums. A subsequence of nums is called a square streak if:

#The length of the subsequence is at least 2, and
#after sorting the subsequence, each element (except the first element) is the square of the previous number.
#Return the length of the longest square streak in nums, or return -1 if there is no square streak.

#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: nums = [4,3,6,16,8,2]
#Output: 3
#Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
#- 4 = 2 * 2.
#- 16 = 4 * 4.
#Therefore, [4,16,2] is a square streak.
#It can be shown that every subsequence of length 4 is not a square streak.



#my own solution using python3:

#use binary search to find everything from left of i to beg that's equal to sqrt(i's value)

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        nums.sort()
        cur = nums.copy()
        biggest = -1
        for i in range(len(nums) -1, -1, -1):
            cur.pop()
            s = math.sqrt(nums[i])
            b = bisect_left(cur, s)
            if nums[b] ** 2 == nums[i]: 
                dp[b] = dp[i] + 1
        print(dp)
        if max(dp) == 1:
            return -1
        return max(dp)
