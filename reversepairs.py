#493
#hard

#Given an integer array nums, return the number of reverse pairs in the array.

#A reverse pair is a pair (i, j) where:

#0 <= i < j < nums.length and
#nums[i] > 2 * nums[j].
 

#Example 1:

#Input: nums = [1,3,2,3,1]
#Output: 2
#Explanation: The reverse pairs are:
#(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
#(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1


#my own solution using python3:

#use sorted list and binary search to find the exact point you want, and be sure not to double count pairs!

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList(nums)
        ans = 0
        for i in range(len(nums)):
            sl.discard(nums[i])
            cur = 0
            l, r = 0, len(sl) - 1
            while l <= r:
                mid = (l + r) // 2
                val = sl[mid]
                if nums[i] > 2 * val:
                    cur = max(cur, mid + 1)
                    l = mid + 1
                else:
                    r = mid - 1
            ans += cur
            
               

        return ans
