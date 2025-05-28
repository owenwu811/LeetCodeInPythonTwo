#2426
#hard

#You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:

#0 <= i < j <= n - 1 and
#nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
#Return the number of pairs that satisfy the conditions.

 

#Example 1:

#Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
#Output: 3
#Explanation:
#There are 3 pairs that satisfy the conditions:
#1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
#2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
#3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
#Therefore, we return 3.


#my own solution using python3:

#rearrange the equation - if the difference between cur index vs differences between cur indexes to the right plus difference is less than or equal to the cur diff, then += 1

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        d = []
        ans = 0
        for i, n in enumerate(nums1):
            d.append(nums1[i] - nums2[i] + diff)
        sl = SortedList(d)
        for i, n in enumerate(nums1):
            nowd = n - nums2[i]
            sl.discard(nowd + diff)
            bl = bisect_left(sl, nowd)
            ans += (len(sl) - bl)
            #for a in d[i + 1:]:
            #    if nowd <= a:
            #        ans += 1
        return ans
