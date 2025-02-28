
#3460
#medium

#You are given two strings s and t.

#Return the length of the longest common prefix between s and t after removing at most one character from s.

#Note: s can be left without any removal.

 

#Example 1:

#Input: s = "madxa", t = "madam"

#Output: 4

#Explanation:

#Removing s[3] from s results in "mada", which has a longest common prefix of length 4 with t.





#correct python3 solution (could not solve):

class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j += 1
            elif i == j:
                continue
            else:
                break
        return j
