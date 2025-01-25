
#3210
#easy

#You are given a string s and an integer k. Encrypt the string using the following algorithm:

#For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
#Return the encrypted string.

 

#Example 1:

#Input: s = "dart", k = 3

#Output: "tdar"

#Explanation:

#For i = 0, the 3rd character after 'd' is 't'.
#For i = 1, the 3rd character after 'a' is 'd'.
#For i = 2, the 3rd character after 'r' is 'a'.
#For i = 3, the 3rd character after 't' is 'r'.


#my own solution using python3:

#reset the value to 0 if you are over the length of s to make it cyclic

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        new = list(s)
        modify = new.copy()
        for i in range(len(modify)):
            modify[i] = new[(i + k) % len(s)]
        print(modify)
        return "".join(modify)
