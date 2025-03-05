
#3355
#medium

#You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

#For each queries[i]:

#Select a subset of indices within the range [li, ri] in nums.
#Decrement the values at the selected indices by 1.
#A Zero Array is an array where all elements are equal to 0.

#Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

#Input: nums = [1,0,1], queries = [[0,2]]

#Output: true

#Explanation:

#For i = 0:
#Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
#The array will become [0, 0, 0], which is a Zero Array.


#my own solution using python3:

#use difference array technique

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        orig = [0] * len(nums)
        for q in queries:
            start, end = q[0], q[1]
            orig[start] -= 1
            if end + 1 < len(orig):
                orig[end + 1] += 1
        print(orig)
        p = list(itertools.accumulate(orig))
        print(p)
        for i, n in enumerate(nums):
            nums[i] += p[i]
        print(nums)
        for i, n in enumerate(nums):
            if n > 0:
                return False
        return True

