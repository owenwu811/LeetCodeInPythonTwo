#1646
#easy

#You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

#nums[0] = 0
#nums[1] = 1
#nums[2 * i] = nums[i] when 2 <= 2 * i <= n
#nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
#Return the maximum integer in the array nums​​​.

 

#Example 1:

#Input: n = 7
#Output: 3
#Explanation: According to the given rules:
#  nums[0] = 0
#  nums[1] = 1
#  nums[(1 * 2) = 2] = nums[1] = 1
#  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
#  nums[(2 * 2) = 4] = nums[2] = 1
#  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
#  nums[(3 * 2) = 6] = nums[3] = 2
#  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
#Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.


#my own solution using python3:

#follow the instructions carefully

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        length = n + 1
        if n <= 1:
            return n
        if n >= 2:
            cur = [0] * (n + 1)    
            cur[0] = 0
            cur[1] = 1
            for i in range(len(cur)):
                if 2 <= 2 * i <= len(cur) - 1:
                    cur[2 * i] = cur[i]
                if 2 <= 2 * i + 1 <= len(cur) - 1:
                    cur[2 * i + 1] = cur[i] + cur[i + 1]
            print(cur)
            return max(cur)
