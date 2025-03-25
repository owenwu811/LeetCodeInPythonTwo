#491
#medium

#Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

#Example 1:

#Input: nums = [4,6,7,7]
#Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#Example 2:

#Input: nums = [4,4,3,2,1]
#Output: [[4,4]]



#my own solution using python3:

#just get every combination of every length and make sure it's sorted - don't forget the original input

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) -1, -1, -1):
            for a in combinations(nums, i):
                if len(a) >= 2 and list(a) == list(sorted(a)):
                    print(a)
                    now = list(a).copy()
                    if now not in res:
                        res.append(now)
        res.sort()
        print(res)
        if nums == sorted(nums) and len(nums) >= 2:
            res.append(nums)
        return res
