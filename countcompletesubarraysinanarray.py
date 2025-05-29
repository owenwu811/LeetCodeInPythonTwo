
#2799
#medium

#You are given an array nums consisting of positive integers.

#We call a subarray of an array complete if the following condition is satisfied:

#The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
#Return the number of complete subarrays.

#A subarray is a contiguous non-empty part of an array.

 

#Example 1:

#Input: nums = [1,3,1,2,2]
#Output: 4
#Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
#Example 2:

#Input: nums = [5,5,5,5]
#Output: 10
#Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.


#my own solution using python3 on 5/28/25 - originally solved on August, 8, 2024 but forgot to log the file:

#just use n ^ 2 since the size of the array is small

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        key = set(nums)
        #{1, 2, 3}
        ans = 0
        for i in range(len(nums)):
            c = set()
            for j in range(i, len(nums)):
                c.add(nums[j])
                if key == c:
                    ans += 1
        return ans
