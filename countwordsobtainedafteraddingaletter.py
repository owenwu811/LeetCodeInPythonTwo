
#2135
#medium

#You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

#For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

#The conversion operation is described in the following two steps:

#Append any lowercase letter that is not present in the string to its end.
#For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
#Rearrange the letters of the new string in any arbitrary order.
#For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
#Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

#Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.

 

#Example 1:

#Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]

#my own solution using python3:

#just use the star pattern and sort each string

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sd = dict()
        for s in startWords:
            sd["".join(sorted(s))] = s
        ans = 0
        for t in targetWords:
            flag = False
            for j in range(len(t)):
                pattern = "".join(sorted(t[:j] + t[j + 1:]))
                if pattern in sd:
                    flag = True
                    break
            if flag:
                ans += 1
        return ans
