#3223
#medium

#You are given a string s.

#You can perform the following process on s any number of times:

#Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
#Delete the closest character to the left of index i that is equal to s[i].
#Delete the closest character to the right of index i that is equal to s[i].
#Return the minimum length of the final string s that you can achieve.

#my own solution using python3:

class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        res = 0
        for a, b in c.items():
            if b % 2 == 0:
                res += 2
            else:
                res += 1
        return res 
