
#581
#medium

#Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

#Return the shortest such subarray and output its length.

 

#Example 1:

#Input: nums = [2,6,4,8,10,9,15]
#Output: 5
#Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

#my own solutuion using python3:

#just keep track of the longest range that has differences

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        print(nums)
        a = sorted(nums)
        print(a)
        res = 0
        totdiff = 0
        cur = []
        for i in range(len(nums)):
            if nums[i] != a[i]:
                cur.append(i)
        print(cur)
        if not cur:
            return 0 
        return cur[-1] - cur[0] + 1
