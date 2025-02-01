#3438
#easy

#You are given a string s consisting only of digits. A valid pair is defined as two adjacent digits in s such that:

#The first digit is not equal to the second.
#Each digit in the pair appears in s exactly as many times as its numeric value.
#Return the first valid pair found in the string s when traversing from left to right. If no valid pair exists, return an empty string.

 

#Example 1:

#Input: s = "2523533"

#Output: "23"

#Explanation:

#Digit '2' appears 2 times and digit '3' appears 3 times. Each digit in the pair "23" appears in s exactly as many times as its numeric value. Hence, the output is "23".


#my own solution using python3:

#simply check every pair along with the frequency requirements and return the first matching one from left to right

class Solution:
    def findValidPair(self, s: str) -> str:
        for i in range(1, len(s)):
            if s[i] != s[i - 1] and s.count(s[i]) == int(s[i]) and s.count(s[i - 1]) == int(s[i - 1]):
                return s[i - 1: i + 1]
        return ""
