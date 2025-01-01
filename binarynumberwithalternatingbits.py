
#693
#easy

#Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

#Example 1:

#Input: n = 5
#Output: true
#Explanation: The binary representation of 5 is: 101
#Example 2:

#Input: n = 7
#Output: false
#Explanation: The binary representation of 7 is: 111.
#Example 3:

#Input: n = 11
#Output: false
#Explanation: The binary representation of 11 is: 1011.


#my own solution using python3:

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = str(bin(int(n))[2:])
        print(s)
        if len(s) == 2:
            return s[0] != s[1]
        for i in range(1, len(s) - 1):
            if s[i] == s[i - 1] or s[i] == s[i + 1]:
                return False
        return True
