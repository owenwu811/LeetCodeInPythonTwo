


#392
#easy

#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


#could not solve (correct python3 solution):

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        one, two = 0, 0
        res = 0
        while one < len(s) and two < len(t):
            if s[one] == t[two]:
                one += 1
                res += 1
            two += 1
        return res == len(s)


#1/23/25 review:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        res = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
                res += 1
            r += 1
        return res == len(s)
