#2839
#easy

#You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

#You can apply the following operation on any of the two strings any number of times:

#Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
#Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

#Example 1:

#Input: s1 = "abcd", s2 = "cdab"
#Output: true
#Explanation: We can do the following operations on s1:
#- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
#- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.


#my own solution using python3:

#brute force through both strings

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        first = list(s1)
        second = list(s2)
        origf, origs = first.copy(), second.copy()
        for i in range(len(first)):
            for j in range(len(first)):
                if abs(j - i) == 2:
                    print(i, j)
                    first[i], first[j] = first[j], first[i]
                    print(first)
                    if first == second:
                        return True  
        for i in range(len(second)):
            for j in range(len(second)):
                if abs(j - i) == 2:
                    second[i], second[j] = second[j], second[i]
                    if second == origf:
                        return True  
                    second[:] = origs
        return False
