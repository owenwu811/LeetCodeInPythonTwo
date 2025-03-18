#3481
#medium

#You are given a replacements mapping and a text string that may contain placeholders formatted as %var%, where each var corresponds to a key in the replacements mapping. Each replacement value may itself contain one or more such placeholders. Each placeholder is replaced by the value associated with its corresponding replacement key.

#Return the fully substituted text string which does not contain any placeholders.

 

#Example 1:

#Input: replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"

#Output: "abc_def"

#correct python3 solution (could not solve):

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        for i in range(len(replacements)):
            for a, b in replacements:
                text = text.replace(f"%{a}%", b)
        return text
