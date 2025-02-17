#3010
#easy

#You are given an array of integers nums of length n.

#The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

#You need to divide nums into 3 disjoint contiguous 
#subarrays
#.

#Return the minimum possible sum of the cost of these subarrays.

 

#Example 1:

#Input: nums = [1,2,3,12]
#Output: 6
#Explanation: The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
#The other possible ways to form 3 subarrays are:
#- [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
#- [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.

#my own solution using python3:

#follow the instructions by getting all combinations of 3 cuts in the array 

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                first = nums[:i]
                second = nums[i: j + 1]
                third = nums[j:]
                if first and second and third:
                    #print(first, second, third)
                    res = min(res, first[0] + second[0] + third[0])
        return res
