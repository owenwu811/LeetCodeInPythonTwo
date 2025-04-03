
#1891
#medium

#You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

#For example, if you have a ribbon of length 4, you can:
#Keep the ribbon of length 4,
#Cut it into one ribbon of length 3 and one ribbon of length 1,
#Cut it into two ribbons of length 2,
#Cut it into one ribbon of length 2 and two ribbons of length 1, or
#Cut it into four ribbons of length 1.
#Your task is to determine the maximum length of ribbon, x, that allows you to cut at least k ribbons, each of length x. You can discard any leftover ribbon from the cuts. If it is impossible to cut k ribbons of the same length, return 0.

 

#Example 1:

#Input: ribbons = [9,7,5], k = 3
#Output: 5


#my own solution using python3:

#lots of trial and error

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        res = 0
        l, r = 1, max(ribbons)
        ribbons.sort()
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for r in ribbons:
                now = ceil(r // mid)
                cur += now
            if cur >= k:
                l = mid + 1
                print(mid)
                res = max(res, mid)
            else:
                r = mid - 1
        return res
