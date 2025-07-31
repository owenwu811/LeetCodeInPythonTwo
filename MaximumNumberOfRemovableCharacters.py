#1898
#medium

#You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

#You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

#Return the maximum k you can choose such that p is still a subsequence of s after the removals.

#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

 

#Example 1:

#Input: s = "abcacb", p = "ab", removable = [3,1,0]
#Output: 2
#Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
#"ab" is a subsequence of "accb".
#If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
#Hence, the maximum k is 2.

#my own solution using python3:

#use binary search to find biggest k, and then use two pointers to determine if subsequence

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def issub(p, cur):
            i, j = 0, 0
            cnt = 0
            while i < len(p) and j < len(cur):
                if p[i] == cur[j]:
                    i += 1
                    j += 1
                    cnt += 1
                else:
                    j += 1
            return cnt == len(p)
        def good(val):
            y = list(removable)[:val].copy()
            nn = set(y)
            now = list(s)
            cc = []
            for j in range(len(now)):
                if j in nn:
                    continue
                cc.append(now[j])
            return issub(p, "".join(cc))
        l, r, ans = 0, len(removable), 0
        l, r = 0, len(removable)
        while l <= r:
            mid = (l + r) // 2
            if good(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans
