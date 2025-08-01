#792
#medium

#Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#For example, "ace" is a subsequence of "abcde".
 

#Example 1:

#Input: s = "abcde", words = ["a","bb","acd","ace"]
#Output: 3
#Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
#Example 2:

#Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
#Output: 2

#my own solution using python3:

#use two pointers and loop through set and use dictionary to count how many 

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        def issub(one, two):
            i, j = 0, 0
            cc = 0
            while i < len(one) and j < len(two):
                if one[i] == two[j]:
                    i += 1
                    j += 1
                    cc += 1
                else:
                    j += 1
            return cc == len(one)
        c = Counter(words)
        for w in set(words):
            if issub(w, s):
                cnt += c[w]
        return cnt
