#1438
#medium

#Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

#Example 1:

#Input: nums = [8,2,4,7], limit = 4
#Output: 2 
#Explanation: All subarrays are: 
#[8] with maximum absolute diff |8-8| = 0 <= 4.
#[8,2] with maximum absolute diff |8-2| = 6 > 4. 
#[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
#[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
#[2] with maximum absolute diff |2-2| = 0 <= 4.
#[2,4] with maximum absolute diff |2-4| = 2 <= 4.
#[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
#[4] with maximum absolute diff |4-4| = 0 <= 4.
#[4,7] with maximum absolute diff |4-7| = 3 <= 4.
#[7] with maximum absolute diff |7-7| = 0 <= 4. 
#Therefore, the size of the longest subarray is 2.


#my own solution using python3:

#use a sorted list for quicker sorts to avoid TLE

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        d = SortedList()
        res = 0
        for r in range(len(nums)):
            d.add(nums[r])
            if d[-1] - d[0] <= limit:
                res = max(res, r - l + 1)
            else:
                d.remove(nums[l])
                l += 1
        return res
