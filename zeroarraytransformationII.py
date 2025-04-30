#3356
#medium

#You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

#Each queries[i] represents the following action on nums:

#Decrement the value at each index in the range [li, ri] in nums by at most vali.
#The amount by which each value is decremented can be chosen independently for each index.
#A Zero Array is an array with all its elements equal to 0.

#Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

#Example 1:

#Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

#Output: 2

#my own solution using python3 after using chatgpt (fuck this question):

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isgood(mid):
            cur = [0] * len(nums)
            for j in range(mid):
                s, e, val = queries[j][0], queries[j][1], queries[j][2]
                cur[s] -= val
                if e + 1 < len(cur):
                    cur[e + 1] += val
            a = list(itertools.accumulate(cur))
            #print(a, nums, mid)
            h = nums.copy()
            for i, n in enumerate(h):
                h[i] += a[i]
            #print(mid, h)
            if max(h) <= 0:
                return True
            return False
        l, r = 0, len(queries) 
        ans = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if isgood(mid):
                #print(mid)
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        if ans == float('inf'):
            return -1
        return ans
