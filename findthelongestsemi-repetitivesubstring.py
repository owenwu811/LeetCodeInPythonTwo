#2730
#medium

#You are given a digit string s that consists of digits from 0 to 9.

#A string is called semi-repetitive if there is at most one adjacent pair of the same digit. For example, "0010", "002020", "0123", "2002", and "54944" are semi-repetitive while the following are not: "00101022" (adjacent same digit pairs are 00 and 22), and "1101234883" (adjacent same digit pairs are 11 and 88).

#Return the length of the longest semi-repetitive substring of s.

 

#Example 1:

#Input: s = "52233"

#Output: 4

#Explanation:

#The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.

#my own solution using python3:

#constraints are small, so you can use n squared - just understand the question carefully

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 1
        for i in range(len(s)):
            cnt = 0
            for j in range(i + 1, len(s)):
                if s[j] == s[j - 1]:
                    cnt += 1
                if cnt <= 1:
                    res = max(res, j - i + 1)
        return res
