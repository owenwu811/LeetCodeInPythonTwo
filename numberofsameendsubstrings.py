
#2955
#medium

#You are given a 0-indexed string s, and a 2D array of integers queries, where queries[i] = [li, ri] indicates a substring of s starting from the index li and ending at the index ri (both inclusive), i.e. s[li..ri].

#Return an array ans where ans[i] is the number of same-end substrings of queries[i].

#A 0-indexed string t of length n is called same-end if it has the same character at both of its ends, i.e., t[0] == t[n - 1].

#A substring is a contiguous non-empty sequence of characters within a string.

 

#Example 1:

#Input: s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]
#Output: [1,5,5,10]
#Explanation: Here is the same-end substrings of each query:
#1st query: s[0..0] is "a" which has 1 same-end substring: "a".
#2nd query: s[1..4] is "bcaa" which has 5 same-end substrings: "bcaa", "bcaa", "bcaa", "bcaa", "bcaa".
#3rd query: s[2..5] is "caab" which has 5 same-end substrings: "caab", "caab", "caab", "caab", "caab".
#4th query: s[0..5] is "abcaab" which has 10 same-end substrings: "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab".

#my own solution using python3 using hints:

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        for q in queries:
            start, end = q[0], q[1]
            cur = 0
            for k in d:
                l, r = bisect_left(d[k], start), bisect_right(d[k], end)
                t = (r - l)
                cur += (t * (t + 1) // 2)
            #now = s[start: end + 1]
            #for i, n in enumerate(now):
            #    cur += now[i + 1:].count(n)
            print("done")
            res.append(cur)
        return res
