#2381
#medium


#You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

#Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

#Return the final string after all such shifts to s are applied.

 

#Example 1:

#Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
#Output: "ace"
#Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
#Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
#Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".


#my own solution using python3:

#lots of trial and error and making sure the negative and > 25 shifts are correct

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        p = [0] * len(s)
        d = dict()
        od = dict()
        for i, c in enumerate(letters):
            d[c] = i
            od[i] = c
        orig = []
        for i, c in enumerate(s):
            orig.append(d[c])
        print(orig, "orig")
        for sub in shifts:
            start, end, direction = sub[0], sub[1], sub[2]
            if direction == 1:
                p[start] += 1
                if end + 1 < len(p):
                    p[end + 1] -= 1
            else:
                p[start] -= 1
                if end + 1 < len(p):
                    p[end + 1] += 1
        a = list(itertools.accumulate(p))
        print(a, "a")
        print(orig)
        final = []
        for i, v in enumerate(orig):
            cur = v + a[i] 
            if cur > 25:
                while cur > 25:
                    cur -= 26
            if cur < 0:
                while cur < 0:
                    cur = 26 - abs(cur)
            print(cur)
            final.append(cur)
        print(final)
        ans = []
        for f in final:
            ans.append(od[f])
        return "".join(ans)
