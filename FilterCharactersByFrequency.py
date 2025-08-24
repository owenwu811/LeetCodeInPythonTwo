#3662
#easy

#You are given a string s consisting of lowercase English letters and an integer k.

#Your task is to construct a new string that contains only those characters from s which appear fewer than k times in the entire string. The order of characters in the new string must be the same as their order in s.

#Return the resulting string. If no characters qualify, return an empty string.

#Note: Every occurrence of a character that occurs fewer than k times is kept.

#my own solution using python3:

#just follow the instructions as directed

class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        ans = ""
        for c in s:
            if s.count(c) < k:
                ans += c
        return ans
