#2055
#medium

#There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

#You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

#For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
#Return an integer array answer where answer[i] is the answer to the ith query.

#Input: s = "**|**|***|", queries = [[2,5],[5,9]]
#Output: [2,3]


#my own solution using python3:

#use prefix sum to count how many candles in the substring, and then use binary search to find the leftmost and rightmost candle in the substring

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        candlei = []
        prefc = []
        cc = 0
        for i, a in enumerate(s):
            if a == "|":
                candlei.append(i)
            else:
                cc += 1
            prefc.append(cc)
        res = []
        for q in queries:
            start, e = q[0], q[1]
            l = bisect_left(candlei, start) 
            r = bisect_right(candlei, e)
            now = candlei[l: r]
            if len(now) >= 2 and now[-1] - now[0] > 1:
                left, right = now[0], now[-1]
                a = s[left:right + 1]
                #print(a)
                #print(prefc[left:right + 1])
                if left <= 0:
                    res.append(prefc[right])
                else:
                    res.append(prefc[right - 1] - prefc[left - 1])
                #res.append(a.count("*"))
            else:
                #print("none")
                res.append(0)
        return res
