#3365
#medium


#You are given two strings s and t, both of which are anagrams of each other, and an integer k.

#Your task is to determine whether it is possible to split the string s into k equal-sized substrings, rearrange the substrings, and concatenate them in any order to create a new string that matches the given string t.

#Return true if this is possible, otherwise, return false.

#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

#A substring is a contiguous non-empty sequence of characters within a string.

 

#Example 1:

#Input: s = "abcd", t = "cdab", k = 2

#Output: true


#my own solution using python3:

#break both into sizes, sort, and compare

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        size = len(s) // k
        sparts = []
        tparts = []
        for i in range(0, len(s) - size + 1, size):
            substr = s[i: i + size]
            sparts.append(substr)
        
        for i in range(0, len(t) - size + 1, size):
            substr = t[i: i + size]
            #print(substr)
            tparts.append(substr)
        #print(sparts, tparts)
        sparts.sort()
        tparts.sort()
        print(sparts, tparts)
        for i, c in enumerate(sparts):
            if c != tparts[i]:
                return False
        return True
