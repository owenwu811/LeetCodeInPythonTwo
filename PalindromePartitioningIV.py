#1745
#Hard

#Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

#A string is said to be palindrome if it the same string when reversed.

 

#Example 1:

#Input: s = "abcbdd"
#Output: true
#Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.


#my own solution using python3:

#very easy - just use n ^ 2

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        first = ""
        for i in range(len(s)):
            first += s[i]
            if first != first[::-1]:
                continue
            second = ""
            for j in range(i + 1, len(s)):
                second += s[j]
                if second != second[::-1]:
                    continue
                third = s[j + 1:]
                if first and second and third:
                    if first == first[::-1] and second == second[::-1] and third == third[::-1] and len(first) + len(second) + len(third) == len(s):
                        #print(first, second, third)
                        return True
        return False
