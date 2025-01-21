#1790
#easy

#You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

#Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

#Example 1:

#Input: s1 = "bank", s2 = "kanb"
#Output: true
#Explanation: For example, swap the first character with the last character of s2 to make "bank".

#my own solution using python3:

#just swap characters of the first string and check if, at any point, the list is equal to the list of s2 string

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first, second = list(s1), list(s2)
        firstcopy, secondcopy = first.copy(), second.copy()
        for i in range(len(first)):
            for j in range(len(first)):
                first[i], first[j] = first[j], first[i]
                if first == second:
                    return True
                first[:] = firstcopy
        return False
