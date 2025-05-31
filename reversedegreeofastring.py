#3498
#easy

#Given a string s, calculate its reverse degree.

#The reverse degree is calculated as follows:

#For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
#Sum these products for all characters in the string.
#Return the reverse degree of s.

 

#Example 1:

#Input: s = "abc"

#Output: 148



#my own solution using python3:

#just simulate the instructions

class Solution:
    def reverseDegree(self, s: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        cnt = 0
        ans = 0
        for i in range(len(s)):
            pos = letters.index(s[i])

            print(26 - pos, cnt + 1)
            ans += (26 - pos) * (cnt + 1)
            cnt += 1
        return ans
