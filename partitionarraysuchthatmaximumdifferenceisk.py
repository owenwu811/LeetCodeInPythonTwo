#2294
#medium

#You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

#Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

#A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: nums = [3,6,1,2,5], k = 2
#Output: 2


#my own solution using python3:

#use k == 0 to take care of tle

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        i = 0
        if k == 0:
            return len(set(nums))
        while i < len(nums):
            b = bisect_right(nums[i + 1:], nums[i] + k)
            res += 1
            i += b
            i += 1
            #print(i + 1)
        return res
            
