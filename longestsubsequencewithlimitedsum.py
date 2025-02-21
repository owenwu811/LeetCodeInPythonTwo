#2389
#easy

#You are given an integer array nums of length n, and an integer array queries of length m.

#Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: nums = [4,5,2,1], queries = [3,10,21]
#Output: [2,3,4]
#Explanation: We answer the queries as follows:
#- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
#- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
#- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.



#my own solution using python3:

#use binary search to find how many elements in nums are smaller than the current q

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        s = SortedList(nums)
        p = list(itertools.accumulate(s))
        res = []
        for q in queries:
            cursum = 0
            cnt = 0
            b = bisect_left(p, q)
            if b < len(p):
                if p[b] == q:
                    res.append(b + 1)
                else:
                    res.append(b)
            else:
                res.append(b)
        return res
