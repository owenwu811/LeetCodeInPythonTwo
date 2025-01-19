#3228
#medium

#You are given a 
#binary string
# s.

#You can perform the following operation on the string any number of times:

#Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
#Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
#Return the maximum number of operations that you can perform.


#correct python3 solution (could not solve):

#this still makes zero sense to me...

class Solution:
    def maxOperations(self, s: str) -> int:
        cnt = 0
        ans = 0
        for i in range(len(s) -1, 0, -1):
            if s[i] == "0" and s[i - 1] == "1":
                cnt += 1
                ans += cnt
            elif s[i] == "1" and s[i - 1] == "1":
                ans += cnt    
            print(cnt)
        return ans
