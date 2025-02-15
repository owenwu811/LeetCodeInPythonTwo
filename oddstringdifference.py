#2451
#easy


#You are given an array of equal-length strings words. Assume that the length of each string is n.

#Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

#For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
#All the strings in words have the same difference integer array, except one. You should find that string.

#Return the string in words that has different difference integer array.

 

#Example 1:

#Input: words = ["adc","wzy","abc"]
#Output: "abc"
#Explanation: 
#- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
#- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
#- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
#The odd array out is [1, 1], so we return the corresponding string, "abc".



#my own solution using python3:

#use a dictionary to map the positions of the letters, and then another dictionary to see the lowest count

class Solution:
    def oddString(self, words: List[str]) -> str:
        d = dict()
        letters = "abcdefghijklmnopqrstuvwxyz"
        cnt = 0
        for l in letters:
            d[l] = cnt
            cnt += 1
        print(d)
        myd = defaultdict(list)
        for w in words:
            cur = []
            for i in range(1, len(w)):
                cur.append((d[w[i]] - d[w[i - 1]]))
            print(cur)
            myd[tuple(cur)].append(w)
        print(myd)
        for k in myd:
            if len(myd[k]) == 1:
                return "".join(myd[k])
