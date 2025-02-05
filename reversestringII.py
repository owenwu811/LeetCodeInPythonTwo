
#541
#easy

#Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

#If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

#Example 1:

#Input: s = "abcdefg", k = 2
#Output: "bacdfeg"
#Example 2:

#Input: s = "abcd", k = 2
#Output: "bacd"

#my own solution using python3:

#get the leftover and handle it appropriately

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        res = ""
        size = 2 * k 
        last = 0
        for i in range(0, len(s) - size + 1, size):
            substr = list(s[i: i + size])
            print(i + size)
            last = i + size
            print(substr)
            changed = substr[:k][::-1] + substr[k:]
            print(changed) 
            res += "".join(changed)
        if last < len(s):
            if len(s[last:]) >= k:
                cur = list(s[last:])
                print(cur)
                cur[:] = cur[:k][::-1] + cur[k:]
                res += "".join(cur)
            else:
                cur = list(s[last:])
                print(cur, "hi")

                res += s[last:][::-1]


        return res
