#3503
#medium


#You are given two strings, s and t.

#You can create a new string by selecting a substring from s (possibly empty) and a substring from t (possibly empty), then concatenating them in order.

#Return the length of the longest palindrome that can be formed this way.

#A substring is a contiguous sequence of characters within a string.

#A palindrome is a string that reads the same forward and backward.

 

#Example 1:

#Input: s = "a", t = "a"

#Output: 2

#Explanation:

#Concatenating "a" from s and "a" from t results in "aa", which is a palindrome of length 2.




#my own solution using python3:

#just follow the exact instructions and use brute force

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        soptions = []
        toptions = []
        res = 1
        if s == s[::-1]:
            res = max(res, len(s))
        if t == t[::-1]:
            res = max(res, len(t))

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if substr == substr[::-1]:
                    res = max(res, len(substr))
                soptions.append(substr)
        for i in range(len(t)):
            for j in range(i, len(t)):
                ss = t[i: j + 1]
                if ss == ss[::-1]:
                    res = max(res, len(ss))
                toptions.append(ss)
        for a in soptions:
            for b in toptions:
                cur = a + b
                if cur == cur[::-1]:
                    #print(cur)
                    res = max(res, len(cur))
        return res
