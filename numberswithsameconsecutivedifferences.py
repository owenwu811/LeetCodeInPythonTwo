#967
#medium

#Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

#Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

 

#Example 1:

#Input: n = 3, k = 7
#Output: [181,292,707,818,929]
#Explanation: Note that 070 is not a valid number, because it has leading zeroes.
#Example 2:

#Input: n = 2, k = 1
#Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


#correct python3 solution (could not solve this stupid question) - fuck backtracking:

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def dfs(cur):
            if len(cur) == n:
                print(cur.copy())
                if int("".join(map(str, cur))) not in ans:
                    ans.append(int("".join(map(str, cur))))
                return 
            now = cur[-1]
            if now + k <= 9:
                cur.append(now + k)
                dfs(cur)
                cur.pop()
            
            if now - k >= 0:
                cur.append(now - k)
                dfs(cur)
                cur.pop()




        for i in range(1, 10):
            dfs([i])
        return ans
