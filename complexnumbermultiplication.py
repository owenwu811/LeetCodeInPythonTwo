


#537
#medium

#A complex number can be represented as a string on the form "real+imaginaryi" where:

#real is the real part and is an integer in the range [-100, 100].
#imaginary is the imaginary part and is an integer in the range [-100, 100].
#i2 == -1.
#Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

#Example 1:

#Input: num1 = "1+1i", num2 = "1+1i"
#Output: "0+2i"
#Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.


#could not solve:


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        
        # Compute real and imaginary parts using formula
        real = a * c - b * d
        imag = a * d + b * c
        
        return f"{real}+{imag}i"
