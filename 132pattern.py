#456
#medium

#Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

#Return true if there is a 132 pattern in nums, otherwise, return false.

 

#Example 1:

#Input: nums = [1,2,3,4]
#Output: false
#Explanation: There is no 132 pattern in the sequence.
#Example 2:

#Input: nums = [3,1,4,2]
#Output: true
#Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#Example 3:

#Input: nums = [-1,3,2,0]
#Output: true
#Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].



#my own solution using python3:

#use a sorted list for the left and right side, and do a binary search to find a value on the right list that is between the smallest of left and cur for the 132 requirement

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        lefts, rights = SortedList(), SortedList(nums)
        n = len(nums)
        for i in range(n):
            lefts.add(nums[i])
            rights.remove(nums[i])
            if i >= 1 and i < n - 1:
                l = lefts[0]
                cur = nums[i]
                low, high = 0, len(rights) - 1
                while low <= high:
                    mid = (low + high) // 2
                    now = rights[mid]
                    if l < now < cur:
                        return True  
                    elif rights[mid] >= cur:
                        high = mid - 1
                    else:
                        low = mid + 1
        return False
