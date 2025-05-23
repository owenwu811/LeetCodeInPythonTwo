#161
#medium

#Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

#A string s is said to be one distance apart from a string t if you can:

#Insert exactly one character into s to get t.
#Delete exactly one character from s to get t.
#Replace exactly one character of s with a different character to get t.
 

#Example 1:

#Input: s = "ab", t = "acb"
#Output: true
#Explanation: We can insert 'c' into s to get t.
#Example 2:

#Input: s = "", t = ""
#Output: false
#Explanation: We cannot get t from s by only one step.

#my own solution using python3:

#just simulate the pattern

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        bad = 0
        for i in range(len(s)):
            if i < len(t):
                if s[i] != t[i]:
                    bad += 1
       #print(bad)
        if bad <= 1 and len(s) == len(t): return True


        for i in range(len(t)):
            pattern = t[:i] + "*" + t[i + 1:]
            r = pattern.replace("*", "")
            #print(r, s)
            if len(r) == 0:
                return True
            if pattern.replace("*", "") == s:
                return True
        for i in range(len(s)):
            pattern = s[:i] + "*" + s[i + 1:]
            r = pattern.replace("*", "")
            #print(r, t)
            if len(r) == 0:
                return True
            if pattern.replace("*", "") == t:
                return True
        return False
