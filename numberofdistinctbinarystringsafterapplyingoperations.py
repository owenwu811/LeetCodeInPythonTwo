
#2450
#medium

#You are given a binary string s and a positive integer k.

#You can apply the following operation on the string any number of times:

#Choose any substring of size k from s and flip all its characters, that is, turn all 1's into 0's, and all 0's into 1's.
#Return the number of distinct strings you can obtain. Since the answer may be too large, return it modulo 109 + 7.

#Note that:

#A binary string is a string that consists only of the characters 0 and 1.
#A substring is a contiguous part of a string.
 

#Example 1:

#Input: s = "1001", k = 3
#Output: 4



#my own solution using python3:

#just see how many subarrays of size k you can get, and power that number, and mod it

class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        mod = ((10 ** 9) + 7)
        #123456789
        #..
        # ..
        #  ..
        curlen = 0
        for i in range(len(s) - k + 1):
            curlen += 1
            #sub = s[i: i + k]
            #d["a"].append(sub)
        return (2 ** curlen) % mod
