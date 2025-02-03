#3442
#easy


#You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:

#One of the characters has an even frequency in the string.
#The other character has an odd frequency in the string.
#Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency.

 

#Example 1:

#Input: s = "aaaaabbc"

#Output: 3

#Explanation:

#The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
#The maximum difference is 5 - 2 = 3.

#my own solution using python3:

#double loop to calculate the requirements - beware of edge case meaning start res at -inf instead of 0 or -1

class Solution:
    def maxDifference(self, s: str) -> int:
        res = float('-inf')
        c = Counter(s)
        h = list(c.keys())
        for i in range(len(h)):
            for j in range(len(h)):
                if i != j:
                    if c[h[i]] % 2 == 0 and c[h[j]] % 2 != 0:
                        res = max(res, c[h[j]] - c[h[i]])
                    
                    if c[h[i]] % 2 != 0 and c[h[j]] % 2 == 0:
                        res = max(res, c[h[i]] - c[h[j]])
        if res == float('-inf'):
            return -1
        return res
