
#809
#medium

#Sometimes people repeat letters to represent extra feeling. For example:

#"hello" -> "heeellooo"
#"hi" -> "hiiii"
#In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

#You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

#For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
#Return the number of query strings that are stretchy.

#Input: s = "heeellooo", words = ["hello", "hi", "helo"]
#Output: 1
#Explanation: 
#We can extend "e" and "o" in the word "hello" to get "heeellooo".
#We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


#my own solution using python3:

#understand the directions carefully and play around with test cases to validate your inputs

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        key = []
        for a, b in groupby(s):
            letter = a
            frequency = len(list(b))
            key.append([letter, frequency])
        print(key, "key")
        res = 0
        #we want to make word equal to s
        for w in words:
            flag = True
            if len(w) > len(s):
                flag = False
            for a in w:
                if a not in s:
                    flag = False
            cur = []
            for a, b in groupby(w):
                letter = a
                frequency = len(list(b))
                cur.append([letter, frequency])
            print("break")
            print(cur)
            if len(cur) < len(key):
                flag = False
            if not flag:
                continue
            for i in range(len(cur)):
                if i < len(cur) and i < len(key):
                    if cur[i][0] != key[i][0]:
                        flag = False
                    if cur[i][0] == key[i][0]:
                        if cur[i][1] < key[i][1]:
                            if key[i][1] < 3:
                                flag = False
                        if cur[i][1] > key[i][1]:
                            flag = False
            if flag:
                res += 1
        return res
