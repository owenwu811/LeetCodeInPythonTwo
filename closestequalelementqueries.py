#3488
#medium


#You are given a circular array nums and an array queries.

#For each query i, you have to find the following:

#The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
#Return an array answer of the same size as queries, where answer[i] represents the result for query i.

 

#Example 1:

#Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

#Output: [2,-1,3]


#my own solution using python3:

#use binary search

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = defaultdict(SortedList)
        now = set()
        tot = len(nums) 
        for q in queries:
            val = nums[q]
            now.add(val)
        for i, n in enumerate(nums):
            if n in now:
                d[n].add(i)
        ans = []
        for q in queries:
            val = nums[q]
            cur = float('inf')
            options = d[val]
            #print(q, options)
            bl = bisect_left(options, q)
            br = bisect_right(options, q)
            #print(bl - 1, br + 1)
            if len(options) < 100:
                for a in options:
                    if a != q:
                        cur = min(cur, abs(tot - q + a), abs(q - a), abs(tot - a + q))
            else:
                for j in range(bl - 1, br + 1):
                    if j >= 0 and j < len(options):
                        a = options[j]
                        if a != q:
                            cur = min(cur, abs(tot - q + a), abs(q - a), abs(tot - a + q), abs(a - q))
            if cur == float('inf'):
                ans.append(-1)
            else:
                ans.append(cur)
        return ans
