#1961
#easy

#Given a string s and an array of strings words, determine whether s is a prefix string of words.

#A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

#Return true if s is a prefix string of words, or false otherwise.

 

#Example 1:

#Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
#Output: true
#Explanation:
#s can be made by concatenating "i", "love", and "leetcode" together.
#Example 2:

#Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
#Output: false
#Explanation:
#It is impossible to make s using a prefix of arr.

#my own solution using python3:

#make sure the ordering is correct as well or else you will fail edge cases

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        cur = []
        if words[0] not in s:
            return False
        for i in range(1, len(words)):
            if words[i] in s and words[i - 1] in s:
                if s.index(words[i]) < s.index(words[i - 1]):
                    return False

        for i, w in enumerate(words):
            if w in s:
                cur.append(i)
                s = s.replace(w, "", 1)
        for i in range(1, len(cur)):
            if cur[i] - cur[i - 1] != 1:
                return False
        return not s
