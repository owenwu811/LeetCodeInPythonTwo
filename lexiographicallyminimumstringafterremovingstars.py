
#3170
#medium

#You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

#While there is a '*', do the following operation:

#Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
#Return the lexicographically smallest resulting string after removing all '*' characters.

 

#Example 1:

#Input: s = "aaba*"
#
#Output: "aab"

#Explanation:

#We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.


#my own solution using python3:

#lots of trial and error:

class Solution:
    def clearStars(self, s: str) -> str:
        sl = SortedList()
        stack = []
        if "*" not in s:
            return s
        idx = s.rfind("*")
        #print(idx)
        cnt = s.count("*")
        for i, c in enumerate(s):
            if c == "*":
                #print(sl)
                cnt -= 1
                del sl[0]
            else:
                sl.add((c, -i))
            if cnt == 0:
                break
        #print(sl)
        h = SortedList()
        for ss in sl:
            h.add((-ss[1], ss[0]))
        #print(h)
        ans = ""
        for a in h:
            ans += a[1]
        
        return ans + s[idx + 1:]
