#315
#hard

#Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

#Example 1:

#Input: nums = [5,2,6,1]
#Output: [2,1,1,0]
#Explanation:
#To the right of 5 there are 2 smaller elements (2 and 1).
#To the right of 2 there is only 1 smaller element (1).
#To the right of 6 there is 1 smaller element (1).
#To the right of 1 there is 0 smaller element.

#my own solution using python3:

#just shows the power of the SortedList()

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        cur = SortedList(nums)
        for i in range(len(nums)):
            cur.remove(nums[i])

            b = bisect_left(cur, nums[i])
            res.append(b)
        return res
