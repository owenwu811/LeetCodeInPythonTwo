
#748
#easy

#Given a string licensePlate and an array of strings words, find the shortest completing word in words.

#A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

#For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

#Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

#Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
#Output: "steps"
#Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
#"step" contains 't' and 'p', but only contains 1 's'.
#"steps" contains 't', 'p', and both 's' characters.
#"stripe" is missing an 's'.
#"stepple" is missing an 's'.
#Since "steps" is the only word containing all the letters, that is the answer.

#my own solution using python3:

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = ""
        print("ah" in "husband")
        for l in licensePlate:
            if l.isdigit() or l == " ":
                continue 
            letters += l.lower()
        letters = "".join(sorted(letters))
        options = []
        shortest = float('inf')
        for w in words:
            cur = "".join(sorted(w))
            print(cur, letters, w)
            if Counter(letters) <= Counter(cur):
                options.append(w)
                shortest = min(shortest, len(w))
        new = []
        for o in options:
            if len(o) == shortest:
                new.append(o)
        return new[0]
