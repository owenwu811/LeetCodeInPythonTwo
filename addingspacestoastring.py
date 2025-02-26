#2109
#medium

#You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

#For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
#Return the modified string after the spaces have been added.

 

#Example 1:

#Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
#Output: "Leetcode Helps Me Learn"
#Explanation: 
#The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
#We then place spaces before those characters.



#my own solution using python3:

#check if the current index is in spaces or not - use set to avoid tle - if it is in spaces, then add a " " before adding the current string character

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        hs = set(spaces)
        for i in range(len(s)):
            if i in hs:
                res.append(" ")
            res.append(s[i])
        print(res)
        return "".join(res)
