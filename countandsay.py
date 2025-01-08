
#38
#medium

#The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

#countAndSay(1) = "1"
#countAndSay(n) is the run-length encoding of countAndSay(n - 1).
#Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

#Given a positive integer n, return the nth element of the count-and-say sequence.

 

#Example 1:

#Input: n = 4

#Output: "1211"

#Explanation:

#countAndSay(1) = "1"
#countAndSay(2) = RLE of "1" = "11"
#countAndSay(3) = RLE of "11" = "21"
#countAndSay(4) = RLE of "21" = "1211"

#my own solution using python3


#make sure you are adding the frequency and then the actual number of the previous iteration!


class Solution:
    def countAndSay(self, n: int) -> str:
        #n = 1 > 1
        #n = 2 > 11 > next would be 1211 because you are adding everything currently as string compression, so one two + one one
        #n = 3 > 11 means we have TWO ones > 2 (two) 1 (ones) > 21

        #so 21 really translates to having 1 two and 1 one, which is 1 2 1 1

        #n = 4 > 21 means we have 1 (one) 2 (two) and 1 (one) 1(one) > 1211

        #n = 5 > 1211 >  1 1 1 2 2 1 (we have one one , two ones, one two, one one)

        d = {"one": "1", "two": "2", "three": "3", "four": "4"}
        myd = {"1": "one", "2": "two"}
        #1 > 11
        #11 > 21
        #21 > 1211
        
        res = "1"
        for i in range(2, n + 1):
            cur = []
            for a, b in groupby(res):
                cur.append([len(list(b)), a])
            print(cur, res)
            res = ""
            for c in cur:
                res += str(c[0])
                res += str(c[1])
        return res
                

