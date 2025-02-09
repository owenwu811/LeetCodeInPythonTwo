#3073
#medium

#Given an array nums, return the maximum value of a triplet (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].

#The value of a triplet (i, j, k) is nums[i] - nums[j] + nums[k].

 

#Example 1:

#Input: nums = [5,6,9]

#Output: 8

#Explanation: We only have one choice for an increasing triplet and that is choosing all three elements. The value of this triplet would be 5 - 6 + 9 = 8.



#my own solution using python3:

#use a sorted list for the left half and the right half - both excluding the current element - and then you know that the right half's last element is the biggest, which is the one we want since we're trying to maximize the overall value, and then we now have to find the closest number to the current value in the left side that's less than the current value

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        mindiff = float('inf')
        lefts, rights = SortedList(), SortedList(nums)
        for i in range(len(nums)):
            lefts.add(nums[i])
            rights.remove(nums[i])
            #print(lefts, rights)
            jval = nums[i]
            if lefts and rights:
                if jval > lefts[0] and jval < rights[-1]:
                    closestto = jval
                    b = bisect_left(lefts, closestto)
                    t = b - 1
                    cur = lefts[t] - jval
                    res = max(res, (cur + rights[-1]))
        return res
                    
