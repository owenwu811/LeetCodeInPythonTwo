#2957
#medium

#You are given a 0-indexed string word.

#In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.

#Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.

#Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.

 

#Example 1:

#Input: word = "aaaaa"
#Output: 2
#Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
#It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

#my own solution using python3:

#just compare each adjacent character, and if the index value is less than 1, then increment ans and step forward by 2 because each left and right side only needs one flip at most

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        ans = 0
        i = 1 
        while i < len(word):
        #for i in range(1, len(word)):
            if abs(letters.index(word[i]) - letters.index(word[i - 1])) <= 1:
                ans += 1
                i += 2
            else:
                i += 1
        return ans
