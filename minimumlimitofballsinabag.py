
#1760
#medium

#You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

#You can perform the following operation at most maxOperations times:

#Take any bag of balls and divide it into two new bags with a positive number of balls.
#For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
#Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

#Return the minimum possible penalty after performing the operations.

 

#Example 1:

#Input: nums = [9], maxOperations = 2

#correct python3 solution (stupid edge cases):

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        sl = SortedList()
        l, r = 1, max(nums) 
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for n in nums:
                now = (n - 1) // mid
                cur += now
            if cur <= maxOperations:
                #print(mid)
                sl.add(mid)
                r = mid - 1
            else:
                l = mid + 1
        return sl[0]
