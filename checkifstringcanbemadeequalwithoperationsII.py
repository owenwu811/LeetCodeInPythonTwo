#2840
#medium

#You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

#You can apply the following operation on any of the two strings any number of times:

#Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
#Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

#Example 1:

#Input: s1 = "abcdba", s2 = "cabdab"
#Output: true
#Explanation: We can apply the following operations on s1:
#- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
#- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
#- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.


#my own solution using python3:

#just compare even and odd indicies

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        evenone = []
        eventwo = []
        oddone = []
        oddtwo = []
        for i, c in enumerate(s1):
            if i % 2 == 0:
                evenone.append(c)
            else:
                oddone.append(c)
        for i, c in enumerate(s2):
            if i % 2 == 0:
                eventwo.append(c)
            else:
                oddtwo.append(c)
        print(evenone, eventwo)
        print(oddone, oddtwo)
        return sorted(evenone) == sorted(eventwo) and sorted(oddone) == sorted(oddtwo)
        
