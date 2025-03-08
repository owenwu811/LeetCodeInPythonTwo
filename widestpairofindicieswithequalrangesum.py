#1983
#medium

#You are given two 0-indexed binary arrays nums1 and nums2. Find the widest pair of indices (i, j) such that i <= j and nums1[i] + nums1[i+1] + ... + nums1[j] == nums2[i] + nums2[i+1] + ... + nums2[j].

#The widest pair of indices is the pair with the largest distance between i and j. The distance between a pair of indices is defined as j - i + 1.

#Return the distance of the widest pair of indices. If no pair of indices meets the conditions, return 0.

 

#Example 1:

#Input: nums1 = [1,1,0,1], nums2 = [0,1,1,0]
#Output: 3
#Explanation:
#If i = 1 and j = 3:
#nums1[1] + nums1[2] + nums1[3] = 1 + 0 + 1 = 2.
#nums2[1] + nums2[2] + nums2[3] = 1 + 1 + 0 = 2.
#The distance between i and j is j - i + 1 = 3 - 1 + 1 = 3.

#correct python3 solution (could not solve):

class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        cur = 0
        memory = {0: -1}
        ans = 0
        for i, n in enumerate(nums1):
            cur += (nums1[i] - nums2[i])
            print(cur)
            if cur in memory:
                ans = max(ans, i - memory[cur])
            else:
                memory[cur] = i
        return ans
