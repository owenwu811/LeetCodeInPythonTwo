


#3370
#easy

#You are given a positive number n.

#Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

 

#Example 1:

#Input: n = 5

#Output: 7

#Explanation:

#The binary representation of 7 is "111".


#my own solution using python3:

#use a loop and play around with the upper bound - n cubed in this case


class Solution:
    def smallestNumber(self, n: int) -> int:

        for i in range(n, n * n * n):
            cur = bin(i)[2:]
            if len(set(cur)) == 1 and cur[0] == "1":
                return i
        return n
