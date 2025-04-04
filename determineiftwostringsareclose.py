#1657
#medium

#Two strings are considered close if you can attain one from the other using the following operations:

#Operation 1: Swap any two existing characters.
#For example, abcde -> aecdb
#Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#You can use the operations on either string as many times as necessary.

#Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

#Example 1:

#Input: word1 = "abc", word2 = "bca"
#Output: true
#Explanation: You can attain word2 from word1 in 2 operations.
#Apply Operation 1: "abc" -> "acb"
#Apply Operation 1: "acb" -> "bca"


#my own solution using python3:

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        first = Counter(word1)
        second = Counter(word2)
        print(first, second)
        f, s = sorted(first.values()), sorted(second.values())
        return len(word1) == len(word2) and set(word1) == set(word2) and f == s
