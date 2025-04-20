
#3522
#medium

#You are given two arrays, instructions and values, both of size n.

#You need to simulate a process based on the following rules:

#You start at the first instruction at index i = 0 with an initial score of 0.
#If instructions[i] is "add":
#Add values[i] to your score.
#Move to the next instruction (i + 1).
#If instructions[i] is "jump":
#Move to the instruction at index (i + values[i]) without modifying your score.
#The process ends when you either:

#Go out of bounds (i.e., i < 0 or i >= n), or
#Attempt to revisit an instruction that has been previously executed. The revisited instruction is not executed.
#Return your score at the end of the process.

#my own solution using python3:

#literally just follow the instructions

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        ans = 0
        i = 0
        seen = set()
        while i < len(instructions) and i >= 0 and i not in seen:
            if instructions[i] == "add":
                ans += values[i]
                seen.add(i)
                i += 1
            else:
                seen.add(i)
                i += values[i]
        return ans
