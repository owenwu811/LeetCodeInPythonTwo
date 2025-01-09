#1486
#easy

#You are given an integer n and an integer start.

#Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

#Return the bitwise XOR of all elements of nums.

 

#Example 1:

#Input: n = 5, start = 0
#Output: 8
#Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
#Where "^" corresponds to bitwise XOR operator.
#Example 2:

#Input: n = 4, start = 3
#Output: 8
#Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.


#my own solution using python3:

#follow the instructions, but only go up to but not including n (play with output a bit)

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        myarr = []
        for i in range(n):
            myarr.append(start + 2 * i)
            
        print(myarr)
        beg = myarr[0]
        for i in range(1, len(myarr)):
            beg = beg ^ myarr[i]
        return beg
