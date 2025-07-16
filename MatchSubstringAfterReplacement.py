#2301
#Hard

#You are given two strings s and sub. You are also given a 2D character array mappings where mappings[i] = [oldi, newi] indicates that you may perform the following operation any number of times:

#Replace a character oldi of sub with newi.
#Each character in sub cannot be replaced more than once.

#Return true if it is possible to make sub a substring of s by replacing zero or more characters according to mappings. Otherwise, return false.

#A substring is a contiguous non-empty sequence of characters within a string.

 

#Example 1:

#Input: s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]
#Output: true
#Explanation: Replace the first 'e' in sub with '3' and 't' in sub with '7'.
#Now sub = "l3e7" is a substring of s, so we return true.


#my own solution using python3:

#follow the instructions exactly, and dont be afraid of n ^ 2

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        d = defaultdict(set)
        orig = defaultdict(list)
        
        for m in mappings:
            d[m[0]].add(m[1])
        for k in d:
            orig[k] = d[k]
        print(d)
        tot = []
        for k in d:
            tot.append(k)
        size = len(sub)
        for i in range(len(s) - size + 1):
            possible = s[i: i + size]
            #print(sub, possible)
            now = []
            for ss in sub:
                now.append(ss)
            #print(now)
            
            seen = set()
            for j in range(len(sub)):
                if now[j] != possible[j]:
                    if now[j] in d:
                        if possible[j] in d[now[j]]:
                            now[j] = possible[j]
                            seen.add(now[j])
            #print(now, possible)
            if "".join(now) == possible:
                return True


                    
        return False
