#2938
#medium

#There are n balls on a table, each ball has a color black or white.

#You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

#In each step, you can choose two adjacent balls and swap them.

#Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

 

#Example 1:

#Input: s = "101"
#Output: 1
#Explanation: We can group all the black balls to the right in the following way:
#- Swap s[0] and s[1], s = "011".
#Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.



#my own solution using python3 after reading hint:

class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt = 0
        ans = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                cnt += 1
            else:
                ans += cnt
        return ans
