
#3361
#medium

#You are given two strings s and t of the same length, and two integer arrays nextCost and previousCost.

#In one operation, you can pick any index i of s, and perform either one of the following actions:

#Shift s[i] to the next letter in the alphabet. If s[i] == 'z', you should replace it with 'a'. This operation costs nextCost[j] where j is the index of s[i] in the alphabet.
#Shift s[i] to the previous letter in the alphabet. If s[i] == 'a', you should replace it with 'z'. This operation costs previousCost[j] where j is the index of s[i] in the alphabet.
#The shift distance is the minimum total cost of operations required to transform s into t.

#Return the shift distance from s to t.

 

#Example 1:

#Input: s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


#my own solution using python3:

#as long as you simulate correctly, time limits shouldn't be an issue

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        ans = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                target = min(nextCost[letters.index(t[i])], previousCost[letters.index(t[i])])
                targetidx = letters.index(t[i])
                curidx = letters.index(s[i])
                rs = 0
                while curidx != targetidx:
                    #if curidx + 1 < len(nextCost):
                    rs += nextCost[curidx]
                    #else:
                    #    rs += previousCost[curidx]
                    curidx += 1
                    curidx = curidx % 26
                ls = 0
                curidx = letters.index(s[i])
                while curidx != targetidx:
                    #if curidx - 1 < 0:
                    #    ls += nextCost[curidx]
                    #else:
                    ls += previousCost[curidx]
                    curidx -= 1
                    if curidx < 0:
                        curidx = 26 - abs(curidx)
                    #print(curidx)
                ans += min(ls, rs)
        return ans
