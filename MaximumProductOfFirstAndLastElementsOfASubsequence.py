#3584
#medium

#You are given an integer array nums and an integer m.

#Return the maximum product of the first and last elements of any subsequence of nums of size m.

 

#Example 1:

#Input: nums = [-1,-9,2,3,-2,-3,1], m = 1

#Output: 81

#Explanation:

#The subsequence [-9] has the largest product of the first and last elements: -9 * -9 = 81. Therefore, the answer is 81.

#my own solution using python3:

#since size m, just look at cur + m to the end, and find the min and max times cur value to take care of negatives

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = float('-inf')
        after = deque(nums[m - 1:])
        sl = SortedList(after)
        for i, n in enumerate(nums):
            if after:
                ans = max(ans, nums[i] * sl[-1], nums[i] * sl[0])
            if after:
                val = after[0]
                sl.discard(val)
                after.popleft()
        return ans
