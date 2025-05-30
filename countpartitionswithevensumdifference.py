
#3432
#easy

#You are given an integer array nums of length n.

#A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

#Left subarray contains indices [0, i].
#Right subarray contains indices [i + 1, n - 1].
#Return the number of partitions where the difference between the sum of the left and right subarrays is even.

 

#Example 1:

#Input: nums = [10,10,3,7,6]

#Output: 4

#Explanation:

#The 4 partitions are:

#[10], [10, 3, 7, 6] with a sum difference of 10 - 26 = -16, which is even.
#[10, 10], [3, 7, 6] with a sum difference of 20 - 16 = 4, which is even.
#[10, 10, 3], [7, 6] with a sum difference of 23 - 13 = 10, which is even.
#[10, 10, 3, 7], [6] with a sum difference of 30 - 6 = 24, which is even.


#my own solution using python3 (contest problem solved during contest on January 25th, 2025):

#get the left sum and the right sum of both sides at each index and just follow the instructions

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        #You are given an integer array nums of length n.

       # A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

        #Left subarray contains indices [0, i].
        #Right subarray contains indices [i + 1, n - 1].
        #Return the number of partitions where the difference between the sum of the left and right subarrays is even.
        #[10,10,3,7,6]
        leftsum = 0
        rightsum = 0
        res = 0
        for i in range(len(nums) - 1):
            leftsum += nums[i]
            rightsum = sum(nums[i + 1:])
            print(leftsum, rightsum, i)
            diff = leftsum - rightsum
            if diff % 2 == 0:
                res += 1
        return res

