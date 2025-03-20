#592
#medium

#Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

#The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

#Example 1:

#Input: expression = "-1/2+1/2"
#Output: "0/1"



#my own solution using python3:

#use Fraction class

from fractions import Fraction

class Solution:
    def fractionAddition(self, e: str) -> str:
        a = eval(e)
        f = Fraction(str(a)).limit_denominator()
        ans = str(f)
        if "/" not in ans:
            return ans + "/" + "1"
        return str(f)
        
