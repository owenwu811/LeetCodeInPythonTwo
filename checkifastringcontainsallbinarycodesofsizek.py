
#1461
#medium

#Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

#Example 1:

#Input: s = "00110110", k = 2
#Output: true
#Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.


#correct python3 solution (could not solve):

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cnt = 2 ** k
        seen = set()
        for i in range(len(s) - k + 1):
            substr = s[i: i + k]
            seen.add(substr)
        return len(seen) >= cnt
