#1930
#medium


#Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

#Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

#A palindrome is a string that reads the same forwards and backwards.

#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#For example, "ace" is a subsequence of "abcde".
 

#Example 1:

#Input: s = "aabca"
#Output: 3
#Explanation: The 3 palindromic subsequences of length 3 are:
#- "aba" (subsequence of "aabca")
#- "aaa" (subsequence of "aabca")
#- "aca" (subsequence of "aabca")


#my own solution using python3:

#take advantage of the fact that there are only 26 letters 

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #aaa
        #aba
        ans = 0
        seen = set()
        d = dict()
        od = defaultdict(SortedList)
        for i, v in enumerate(s):
            d[i] = v
            od[v].add(i)
        for i in range(len(s)): 
            del d[i]
            od[s[i]].remove(i)
            if not od[s[i]]:
                del od[s[i]]
            if s[i] not in od:
                continue
            for k in od:
                if k != s[i]:
                    if od[k][0] < od[s[i]][-1]:
                        seen.add(s[i] + k + s[i])
                else:
                    if len(od[k]) >= 2:
                        seen.add(s[i] + s[i] + s[i])
        return len(seen)
