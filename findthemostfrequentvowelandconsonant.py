
#3541
#easy

#You are given a string s consisting of lowercase English letters ('a' to 'z').

#Your task is to:

#Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
#Find the consonant (all other letters excluding vowels) with the maximum frequency.
#Return the sum of the two frequencies.

#Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

#The frequency of a letter x is the number of times it occurs in the string.
 

#Example 1:

#Input: s = "successes"

#Output: 6

#Explanation:

#The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
#The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
#The output is 2 + 4 = 6.



#my own solution using python3:

#just count up all the frequencies of vowels and nonvowels

class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        print(c)
        biggestv, biggestc = float('-inf'), float('-inf')
        vowels = "aeiou"
        for a, b in c.items():
            if a in vowels:
                biggestv = max(biggestv, b)
            else:
                biggestc = max(biggestc, b)
        print(biggestv, biggestc)
        if biggestv == float('-inf'):
            return biggestc
        elif biggestc == float('-inf'):
            return biggestv
        return biggestv + biggestc
