




#1685

#medium

#You are given an integer array nums sorted in non-decreasing order.

#Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

#In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

#Example 1:

#Input: nums = [2,3,5]
#Output: [4,3,5]
#Explanation: Assuming the arrays are 0-indexed, then
#result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
#result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
#result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.


#my own solution using python3 on 2/26/25:

#use binary search to find bigger half - cur * len of bigger half minus cur * len(smallerhalf) - sum of smaller half

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        p = list(itertools.accumulate(nums))
        biggest = p[-1]
        res = []
        n = len(nums)
        for i in range(len(nums)):
            cur = nums[i]
            now = 0
            l = bisect_left(s, cur)
            r = bisect_right(s, cur)
            if l > 0:
                low = p[l - 1]
                high = cur * l
                now += (high - low)
            if r < n:
                low = cur * (n - r)
                if r <= 0:
                    high = biggest
                else:
                    high = biggest - p[r - 1]
                now += (high - low)
            res.append(now)
        return res



#another dumb question that tests whether or not you can memorize tricks....


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        curr_sum = 0
        tot = sum(nums)
        res = [0] * n
        for i in range(len(nums)):
            curr_sum += nums[i]
            leftsum = curr_sum - nums[i]
            right_sum = tot - curr_sum
            res[i] = right_sum - nums[i] * (len(nums) - i - 1) + nums[i] * (i) - leftsum
        return res
        
