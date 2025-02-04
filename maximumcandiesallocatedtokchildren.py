#2226
#medium

#You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

#You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.

#Return the maximum number of candies each child can get.

 

#Example 1:

#Input: candies = [5,8,6], k = 3
#Output: 5
#Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
#Example 2:

#Input: candies = [2,5], k = 11
#Output: 0
#Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.

#my own solution using python3 after looking at another solution understand what the question was asking:

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        res = 0
        #5 / 3 + 8 / 3 + 6 / 3 = 2 + 3 + 2 = 7
        candies.sort()
        l, r = 1, max(candies)
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for c in candies:
                cur += (c // mid)
            if cur >= k:
                print(mid)
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res
