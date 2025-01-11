
#643
#easy

#You are given an integer array nums consisting of n elements, and an integer k.

#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

#Example 1:

#Input: nums = [1,12,-5,-6,50,3], k = 4
#Output: 12.75000
#Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#Example 2:

#Input: nums = [5], k = 1
#Output: 5.00000


#my own solution using python3:

#instead of computing every sliding window of sized k fixed size, just use prefix sums and subtract the current window end from the window start minus 1 to get the current window sum

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        prefix = list(itertools.accumulate(nums))
        for i in range(len(prefix) - k + 1):
            subarr = prefix[i: i + k]
            if i <= 0:
                cur = prefix[i + k - 1]
            elif i > 0:
                cur = prefix[i + k - 1] - prefix[i - 1]
            res = max(res, cur / len(subarr))
        return res
