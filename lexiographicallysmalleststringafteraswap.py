
#3216
#easy

#Given a string s containing only digits, return the 
#lexicographically smallest string
# that can be obtained after swapping adjacent digits in s with the same parity at most once.

#Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

 

#Example 1:

#Input: s = "45320"

#Output: "43520"

#Explanation:

#s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.


#my own solution using python3:

#just be sure to sort the results at the end and to include the original string as well

class Solution:
    def getSmallestString(self, s: str) -> str:
        res = []
        res.append(s)
        orig = list(s)
        h = orig.copy()
        for i in range(len(orig) - 1):
            j = i + 1
            first = int(orig[i])
            second = int(orig[j])
            if first % 2 == 0 and second % 2 == 0 or first % 2 != 0 and second % 2 != 0:
                orig[i], orig[j] = orig[j], orig[i]
                print(orig)
                res.append("".join(orig))
            orig[:] = h
        res.sort()
        print(res)
        if not res:
            return s
        return res[0]
