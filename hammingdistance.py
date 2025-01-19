
#461
#easy

#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

#Given two integers x and y, return the Hamming distance between them.

 

#Example 1:

#Input: x = 1, y = 4
#Output: 2
#Explanation:
#1   (0 0 0 1)
#4   (0 1 0 0)
#       ↑   ↑
#The above arrows point to positions where the corresponding bits are different.
#Example 2:

#Input: x = 3, y = 1
#Output: 1



#my own solution using python3:

#turn both into lists, take care of length differences, and compare different values at the same index, and count them

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        first = bin(x)[2:]
        second = bin(y)[2:]
        print(first, second)
        finalfirst = deque()
        finalsecond = deque()
        if len(first) < len(second):
            
            diff = len(second) - len(first)
            while diff > 0:
                finalfirst.append(0)
                diff -= 1
            for f in first:
                finalfirst.append(int(f))
            for s in second:
                finalsecond.append(int(s))
        elif len(first) > len(second): 
            diff = len(first) - len(second)
            while diff > 0:
                finalsecond.append(0)
                diff -= 1
            for f in first:
                finalfirst.append(int(f))
            for s in second:
                finalsecond.append(int(s))
        else:
            for f in first:
                finalfirst.append(int(f))
            for s in second:
                finalsecond.append(int(s))
        print(finalfirst, finalsecond)
        res = 0
        for i in range(len(finalfirst)):
            if finalfirst[i] != finalsecond[i]:
                res += 1
        return res
