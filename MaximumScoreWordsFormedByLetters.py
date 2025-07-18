#1255
#Hard

#Given a list of words, list of  single letters (might be repeating) and score of every character.

#Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

#It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

 

#Example 1:

#Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
#Output: 23
#Explanation:
#Score  a=1, c=9, d=5, g=3, o=2
#Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
#Words "dad" and "dog" only get a score of 21.


#my own solution using python3:

#get the value of each word using 26 letter alphabet before recording in dict. get the total counter value of letters. get all combinations of words, and then see if the counter value of that combination is less than or equal to letters. if is it, it may be valid, so get the full letter value of that combination.

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        c = Counter(letters)
        d = dict()
        alph = "abcdefghijklmnopqrstuvwxyz"
        for word in words:
            curscore = 0
            for letter in word:
                loc = alph.index(letter)
                curscore += score[loc]
            print(word, curscore)
            d[word] = curscore

        ans = 0
        for i in range(1, len(words) + 1):
            for comb in combinations(words, i):
                tot = Counter()
                for word in comb:
                    tot += Counter(word)
                if tot <= c:
                    print(comb)
                    ss = 0
                    for wo in comb:
                        ss += d[wo]
                    ans = max(ans, ss)
        return ans
                    
