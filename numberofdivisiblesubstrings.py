#2950
#medium


#A string is divisible if the sum of the mapped values of its characters is divisible by its length.

#Given a string s, return the number of divisible substrings of s.

#A substring is a contiguous non-empty sequence of characters within a string.

#Input: word = "asdf"
#Output: 6
#Explanation: The table above contains the details about every substring of word, and we can see that 6 of them are divisible.

#my own solution using python3:

#use prefix sums to look up the sum and length to avoid TLE

class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        d = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 2, "f": 3, "g": 3, "h": 3, "i": 4, "j": 4, "k": 4, "l": 5, "m": 5, "n": 5, "o": 6, "p": 6, "q": 6, "r": 7, "s": 7, "t": 7, "u": 8, "v": 8, "w": 8, "x": 9, "y": 9, "z": 9}
        cur = 0
        res = 0
        #1 2  3  4
        #a s  d  f 
        #1 8 10 13

        #a
        #a s

        # sd = (10 - 1) = 9, 3 - 1 = 2
        cur = 0
        pref = []
        for i in range(len(word)):
            cur += d[word[i]]
            pref.append(cur)
        res = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                substr = word[i: j + 1]
                if i <= 0:
                    totsum = pref[j] 
                else:
                    totsum = pref[j] - pref[i - 1]
                length = j - i + 1
                if totsum % length == 0:
                    res += 1
        return res
