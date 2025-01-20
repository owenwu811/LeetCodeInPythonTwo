#856
#medium

#Given a balanced parentheses string s, return the score of the string.

#The score of a balanced parentheses string is based on the following rule:

#"()" has score 1.
#AB has score A + B, where A and B are balanced parentheses strings.
#(A) has score 2 * A, where A is a balanced parentheses string.



#correct python3 solution (could not solve):

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        score = 0
        for i in s:
            if i == "(":
                stack.append(score)
                score = 0
            else:
                x = stack.pop()
                score = x + max(2 * score, 1)
        return score
