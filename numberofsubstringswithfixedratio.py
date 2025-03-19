#2489
#medium

#You are given a binary string s, and two integers num1 and num2. num1 and num2 are coprime numbers.

#A ratio substring is a substring of s where the ratio between the number of 0's and the number of 1's in the substring is exactly num1 : num2.

#For example, if num1 = 2 and num2 = 3, then "01011" and "1110000111" are ratio substrings, while "11000" is not.
#Return the number of non-empty ratio substrings of s.

#Note that:

#A substring is a contiguous sequence of characters within a string.
#Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.
 

#Example 1:

#Input: s = "0110011", num1 = 1, num2 = 2
#Output: 4



#correct python3 solution (could not solve):

class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        zc, oc = 0, 0
        d = defaultdict(int)
        d[0] = 1
        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                zc += 1
            else:
                oc += 1
            diff = (zc * num2) - (oc * num1)
            res += d[diff]
            d[diff] += 1
        return res
