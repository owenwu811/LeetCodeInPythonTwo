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
        res = []
        def dfs(i, cur):
            if len(cur) == n:
                print(cur.copy())
                if cur.copy() not in res:
                    res.append(cur.copy())
                #cur.clear()
                return
            now = cur[-1]
            

            if now + k <= 9:
                add = now + k
                cur.append(add)
                dfs(i + 1, cur)
                cur.pop()
                
            if now - k >= 0:
                minus = now - k
                cur.append(minus)
                dfs(i + 1, cur)
                cur.pop()
      
        cur = []
        for i in range(1, 10):
            cur.clear()
            cur.append(i)
            dfs(i, cur)
            
        print(res)
        ans = []
        for r in res:
            cur = ""
            for a in r:
                cur += str(a)
            print(cur)
            ans.append(int(cur))
        return ans
