
#3456
#easy

#You are given a string s and an integer k.

#Determine if there exists a 
#substring
# of length exactly k in s that satisfies the following conditions:

#The substring consists of only one distinct character (e.g., "aaa" or "bbb").
#If there is a character immediately before the substring, it must be different from the character in the substring.
#If there is a character immediately after the substring, it must also be different from the character in the substring.
#Return true if such a substring exists. Otherwise, return false.

 

#Example 1:

#Input: s = "aaabaaa", k = 3

#Output: true

#Explanation:

#The substring s[4..6] == "aaa" satisfies the conditions.

#It has a length of 3.
#All characters are the same.
#The character before "aaa" is 'b', which is different from 'a'.
#There is no character after "aaa".



#my own solution using python3:

#this question has a lot of edge cases that you have to play around with 

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s) == k and len(set(s)) == 1: return True
        size = k
        for i in range(len(s) - size + 1):
            substr = s[i: i + size]
            end = i + size - 1
            if len(set(substr)) == 1:
                print(substr, i, end)
                after = end + 1
                before = i - 1
                if before >= 0 and after < len(s):
                    if s[before] != substr[0] and s[after] != substr[0]:
                        return True
                elif after < len(s):
                    if s[after] != substr[0]:
                        return True 
                elif before >= 0:
                    if s[before] != substr[0]:
                        return True  
                
                
        return False
