#1624
#easy


#Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

#A substring is a contiguous sequence of characters within a string.

 

#Example 1:

#Input: s = "aa"
#Output: 0
#Explanation: The optimal substring here is an empty substring between the two 'a's.

#my own solution using python3:

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(set(s)) == len(s): #if no duplicates
            return -1
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        print(d)
        res = 0
        for k in d:
            res = max(res, max(d[k]) - min(d[k]) - 1) #-1 if you observe the test cases
        return res
