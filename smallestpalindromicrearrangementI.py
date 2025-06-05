#3517
#medium

#You are given a palindromic string s.

#Return the lexicographically smallest palindromic permutation of s.

 

#Example 1:

#Input: s = "z"

#Output: "z"

#Explanation:

#A string of only one character is already the lexicographically smallest palindrome.

#Example 2:

#Input: s = "babab"

#Output: "abbba"

#Explanation:

#Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.


#my own solution using python3:

#generate the first half

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) % 2 != 0:
            half = (len(s) // 2) 
        else:
            half = (len(s) // 2) 
        fh = "".join(sorted(s[:half]))
        sh = s[half:]
        second = list(sh)
        ans = deque()
        d = defaultdict(list)
        for i, v in enumerate(second):
            d[v].append(i)
        c = Counter(second)
        for i in range(len(fh)):
            if fh[i] in c:
                ans.appendleft(fh[i])
                c[fh[i]] -= 1
                if c[fh[i]] == 0:
                    del c[fh[i]]
                #second.remove(fh[i])
        mid = ""
        for a, b in c.items():
            y = b
            while y > 0:
                mid += a
                y -= 1
        
        return fh + mid + "".join(ans)
