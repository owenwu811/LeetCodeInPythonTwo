#3152
#medium

#An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

#You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
#subarray
# nums[fromi..toi] is special or not.

#Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

#Example 1:

#Input: nums = [3,4,1,2,6], queries = [[0,4]]

#Output: [false]

#Explanation:

#The subarray is [3,4,1,2,6]. 2 and 6 are both even.


#my own solution using python3:

#fill in the gaps for the previous element for each pair - make sure to get the spacing correct

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        p = [0] * len(nums)
        for i in range(1, len(nums)):
            if (nums[i] % 2 == 0 and nums[i - 1] % 2 == 0) or (nums[i] % 2 != 0 and nums[i - 1] % 2 != 0):
                p[i - 1] = 1
        tot = list(itertools.accumulate(p))
        res = []
        for q in queries:
            s, e = q[0], q[1]
            if s == e:
                res.append(True)
                continue
            if s <= 0:
                now = tot[e - 1]
            else:
                now = tot[e - 1] - tot[s - 1]
            if now > 0:
                res.append(False)
            else:
                res.append(True)
        return res
