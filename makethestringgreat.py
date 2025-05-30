#1544
#easy

#Given a string s of lower and upper case English letters.

#A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

#0 <= i <= s.length - 2
#s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
#To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

#Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

#Notice that an empty string is also good.

 

#Example 1:

#Input: s = "leEeetcode"
#Output: "leetcode"
#Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".


#my own solution using python3:

#use a stack to simulate the difference in casing between the current character and what's at the top of the stack, and then pop if needed

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if stack[-1].lower() == c.lower():
                if stack[-1].isupper() and not (c.isupper()) or stack[-1].islower() and not (c.islower()):
                    stack.pop()
                    continue
            stack.append(c)
        print(stack)
        return "".join(stack)
