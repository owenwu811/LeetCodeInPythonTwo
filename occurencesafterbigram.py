#1078
#easy

#Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

#Return an array of all the words third for each occurrence of "first second third".

 

#Example 1:

#Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
#Output: ["girl","student"]
#Example 2:

#Input: text = "we will we will rock you", first = "we", second = "will"
#Output: ["we","rock"]

#my own solution using python3:

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        h = text.split(" ")
        res = []
        print(h)
        s = h
        for i in range(2, len(s)):
            if s[i - 1] == second and s[i - 2] == first:
                print(s[i])
                res.append(s[i])
        return res
