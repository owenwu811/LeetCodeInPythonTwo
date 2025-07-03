#1316
#Hard

#Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).

 

#Example 1:

#Input: text = "abcabcabc"
#Output: 3
#Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".

#my own solution using python3:

#you just see if first half of each substr is equal to 2nd half

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        ans = set()
        d = dict()

        for i in range(len(text)):
            cur = ""
            for j in range(i, len(text)):
                cur += text[j]
                #print(cur)
                half = len(cur) // 2
                if cur[:half] == cur[half:]:
                    #print(cur)
                    ans.add(cur)
        return len(ans)
