#2068
#easy

#Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

#Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

#The frequency of a letter x is the number of times it occurs in the string.

 

#Example 1:

#Input: word1 = "aaaa", word2 = "bccb"
#Output: false
#Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
#The difference is 4, which is more than the allowed 3.

#my own solution using python3:

#use two dictionaries

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        first = defaultdict(int)
        second = defaultdict(int)
        for w in word1:
            first[w] += 1
        for w in word2:
            second[w] += 1
        print(first, second)
        for k in first:
            if k not in second:
                if first[k] > 3:
                    return False
            if abs(first[k] - second[k]) > 3:
                return False
        for k in second:
            if k not in first:
                if second[k] > 3:
                    return False
        return True
