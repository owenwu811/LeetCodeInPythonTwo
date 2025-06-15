#3583
#medium

#You are given an integer array nums.

#A special triplet is defined as a triplet of indices (i, j, k) such that:

#0 <= i < j < k < n, where n = nums.length
#nums[i] == nums[j] * 2
#nums[k] == nums[j] * 2
#Return the total number of special triplets in the array.

#Since the answer may be large, return it modulo 109 + 7.

 

#Example 1:

#Input: nums = [6,3,6]

#Output: 1

#my own solution using python3:

#use a sorted list for the left and right sides, and see how many counts of double on both sides, and then multiply those counts

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ans = 0
        mod = ((10 ** 9) + 7)
        lefts, rights = SortedList(), SortedList(nums[1:])
        lefts.add(nums[0])
        ld = Counter(lefts)
        rd = Counter(rights)
        for i in range(1, len(nums) - 1):
            rights.discard(nums[i])
            rd[nums[i]] -= 1
            if rd[nums[i]] == 0:
                del rd[nums[i]]
            double = nums[i] * 2
            ans += ld[double] * rd[double]
            lefts.add(nums[i])
            ld[nums[i]] += 1
        return ans % mod
