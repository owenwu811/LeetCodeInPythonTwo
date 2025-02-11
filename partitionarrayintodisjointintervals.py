
#915
#medium

#Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

#Every element in left is less than or equal to every element in right.
#left and right are non-empty.
#left has the smallest possible size.
#Return the length of left after such a partitioning.

#Test cases are generated such that partitioning exists.

 

#Example 1:

#Input: nums = [5,0,3,8,6]
#Output: 3
#Explanation: left = [5,0,3], right = [8,6]
#Example 2:

#Input: nums = [1,1,1,0,6,12]
#Output: 4
#Explanation: left = [1,1,1,0], right = [6,12]




#my own solution using python3:

#super easy with a sorted list for the left and right sides

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        res = float('inf')
        lefts, rights = SortedList(), SortedList(nums)
        for i in range(len(nums)):
            rights.remove(nums[i])

            lefts.add(nums[i])
            if lefts and rights:
                #print(lefts, rights)
                if lefts[-1] <= rights[0]:
                    print(lefts, rights)
                    res = min(res, len(lefts))
        if res == float('inf'):
            return 1
        return res
