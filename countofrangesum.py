#327
#hard

#Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

#Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

 

#Example 1:

#Input: nums = [-2,5,-1], lower = -2, upper = 2
#Output: 3
#Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
#Example 2:

#Input: nums = [0], lower = 0, upper = 0
#Output: 1


#my own solution using python3:

#the question asks for how many subarray sums lie between lower and upper, so calculate prefix sums, and binary search to find the subarray sum (current - previous minus 1) inside of current to right to find lower and upper bounds

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        p = list(itertools.accumulate(nums))
        aa = sorted(p)
        for i in range(len(nums)):
            if i >= 1:
                now = p[i - 1]
            else:
                now = 0
            lbound = bisect_left(aa, lower + now)
            rbound = bisect_right(aa, upper + now)
            ans += (rbound - lbound)
            idx = bisect_left(aa, p[i])
            del aa[idx]
        return ans
