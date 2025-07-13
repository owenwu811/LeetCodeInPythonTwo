
#3612
#medium

#You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

#Build a new string result by processing s according to the following rules from left to right:

#If the letter is a lowercase English letter append it to result.
#A '*' removes the last character from result, if it exists.
#A '#' duplicates the current result and appends it to itself.
#A '%' reverses the current result.
#Return the final string result after processing all characters in s.

#my own solution using python3:

#literally just follow the instructions

class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            
            if c == "*":
                if res:
                    res.pop()
            elif c == "#":
                res.extend(res)

            elif c == "%":
                res = res[::-1]
            else:
                res.append(c)
        return "".join(res)
