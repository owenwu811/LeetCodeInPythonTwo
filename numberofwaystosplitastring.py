#1573
#medium

#Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.

#Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.

 

#Example 1:

#Input: s = "10101"
#Output: 4
#Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
#"1|010|1"
#"1|01|01"
#"10|10|1"
#"10|1|01"

#my own solution using python3:

#observe the high and low as the optimal binary search point

class Solution:
    def numWays(self, s: str) -> int:
        mod = ((10 ** 9) + 7)
        tc = s.count("1")
        ps = 0
        cur = []
        for i, c in enumerate(s):
            if c == "1":
                ps += 1
            cur.append(ps)
        ans = 0
        lc = 0
        now = cur[:-1].copy()
        c = Counter(now)
        for i in range(len(s)):
            if now:
                c[now[0]] -= 1
                if c[now[0]] == 0:
                    del c[now[0]]
                now.pop(0)
                
            
            #now = cur[i + 1:-1]
            #print(cur[i], now, cur[-1])
            diff = cur[-1] - cur[i]
            if diff - cur[i] == cur[-1] - diff:
                #print(diff)
                ans += c[diff]

            
            

            
        return ans % mod

  
