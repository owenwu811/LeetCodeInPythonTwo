
#201
#medium

#Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

#Example 1:

#Input: left = 5, right = 7
#Output: 4
#Example 2:

#Input: left = 0, right = 0
#Output: 0
#Example 3:

#Input: left = 1, right = 2147483647
#Output: 0


#correct python3 solution (could not solve):

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return right


#2/9/25 review (could not solve):

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return right
