
#3561
#medium

#You are given a string s consisting of lowercase English letters.

#You must repeatedly perform the following operation while the string s has at least two consecutive characters:

#Remove the leftmost pair of adjacent characters in the string that are consecutive in the alphabet, in either order (e.g., 'a' and 'b', or 'b' and 'a').
#Shift the remaining characters to the left to fill the gap.
#Return the resulting string after no more operations can be performed.

#Note: Consider the alphabet as circular, thus 'a' and 'z' are consecutive.

 

#Example 1:

#Input: s = "abc"

#Output: "c"

#Explanation:

#Remove "ab" from the string, leaving "c" as the remaining string.
#No further operations are possible. Thus, the resulting string after all possible removals is "c".


#my own solution using python3:

#use a stack to simulate the absolute difference of exactly 1, and pop or add based on that

class Solution:
    def resultingString(self, s: str) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        stack = []
        for i in range(len(s)):
            #print(stack, s[i])
            if not stack:
                stack.append(s[i])
            else:
                b = letters.index(s[i]) 
                vv = letters.index(stack[-1]) 
                #print(b, vv)
                if b == 25 and vv == 0:
                    b = -1
                if vv == 25 and b == 0:
                    vv = -1
                if abs(b - vv) == 1:
                    stack.pop()
                else:
                    stack.append(s[i])
        #print(stack)
        return "".join(stack)
