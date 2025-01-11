

#2104
#medium

#You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

#Return the sum of all subarray ranges of nums.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [1,2,3]
#Output: 4
#Explanation: The 6 subarrays of nums are the following:
#[1], range = largest - smallest = 1 - 1 = 0 
#[2], range = 2 - 2 = 0
#[3], range = 3 - 3 = 0
#[1,2], range = 2 - 1 = 1
#[2,3], range = 3 - 2 = 1
#[1,2,3], range = 3 - 1 = 2
#So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.



#my own solution using python3:

#just shows how powerful the sortedlist is in python:


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        cur = SortedList()
        for i in range(len(nums)):
            cur.clear()
            for j in range(i, len(nums)):
                cur.add(nums[j])
                res += (cur[-1] - cur[0])
        return res

