

#2559
#medium

#You are given a 0-indexed array of strings words and a 2D array of integers queries.

#Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

#Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

#Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

#Example 1:

#Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
#Output: [2,3,0]
#Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
#The answer to the query [0,2] is 2 (strings "aba" and "ece").
#to query [1,4] is 3 (strings "ece", "aa", "e").
#to query [1,1] is 0.
#We return [2,3,0].


#my own solution using python3:

#use a dictionary to keep track of the number of strings up to this current point that have begs and ends as vowel letters, and keep track of the current substring by subtracting the current value minus the before value minus one if that is not out of bounds

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        cnt = 0
        vowels = "aeiou"
        for i in range(len(words)):
            if len(words[i]) == 1:
                if words[i][0] in vowels:
                    cnt += 1
            if len(words[i]) > 1:
                if words[i][0] in vowels and words[i][-1] in vowels:
                    cnt += 1
            d[i] = cnt
        print(d)
        res = []
        #{0: 1, 1: 1, 2: 2, 3: 3, 4: 4}
        #[0, 2] > 2
        #[1, 4] > 3
        #[1, 1] > 0
        cur = []

        for q in queries:
            before = q[0] - 1
            after = q[1]
            if before >= 0:
                print(before, after)
                now = d[after] - d[before]
                print(now)
                cur.append(now)
            else:
                print(after)
                now = d[after]
                print(now)
                cur.append(now)
            #if before >= 0:
            #    print(d[after], d[before])
            #else:
            #    print(d[after])
        print(cur)
        return cur
            #
