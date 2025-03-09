#43
#medium


#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

#Example 1:

#Input: num1 = "2", num2 = "3"
#Output: "6"


#my own solution using python3 (originally solved on November 5, 2023 but didn't make a file - resolved on 3/8/5):

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        new = ""
        new += num1
        new += "*"
        new += num2
        return str(eval(new))
