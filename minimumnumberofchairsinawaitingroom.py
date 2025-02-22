
#3168
#easy

#You are given a string s. Simulate events at each second i:

#If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
#If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
#Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

 

#Example 1:

#Input: s = "EEEEEEE"

#Output: 7

#Explanation:

#After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.



#my own solution using python3:

#if you print the overall balance at each step, you will observe a pattern

class Solution:
    def minimumChairs(self, s: str) -> int:
        tot = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "E":
                tot -= 1
            else:
                tot += 1
            print(tot)
            res = max(res, abs(tot))
        return res
