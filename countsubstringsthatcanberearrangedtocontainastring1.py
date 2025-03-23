#3297
#medium

#You are given two strings word1 and word2.

#A string x is called valid if x can be rearranged to have word2 as a prefix.

#Return the total number of valid substrings of word1.

 

#Example 1:

#Input: word1 = "bcca", word2 = "abc"

#Output: 1

#Explanation:

#The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.

#my own solution using python3:

#use sliding window with a dictionary

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        l = 0
        d = Counter()
        key = Counter(word2)
        res = 0
        for r in range(len(word1)):
            d[word1[r]] += 1
            while d >= key and l <= r:
                res += (len(word1) - r)
                d[word1[l]] -= 1
                if d[word1[l]] == 0:
                    del d[word1[l]]
                l += 1
        return res
