

#788
#medium

#An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

#A number is valid if each digit remains a digit after rotation. For example:

#0, 1, and 8 rotate to themselves,
#2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
#6 and 9 rotate to each other, and
#the rest of the numbers do not rotate to any other number and become invalid.
#Given an integer n, return the number of good integers in the range [1, n].

 

#Example 1:

#Input: n = 10
#Output: 4
#Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
#Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.


#my own solution using python3:

#just follow the instructions

class Solution:
    def rotatedDigits(self, n: int) -> int:
        options = list(range(1, n + 1))
        print(options)
        res = 0
        for o in options:
            cur = str(o)
            print(cur)
            if "3" in cur or "4" in cur or "7" in cur:
                continue
            if "2" in cur or "5" in cur or "6" in cur or "9" in cur:
                res += 1
        return res
