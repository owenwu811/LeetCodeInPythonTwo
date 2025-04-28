#2825
#medium

#You are given two 0-indexed strings str1 and str2.

#In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

#Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

#Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

 

#Example 1:

#Input: str1 = "abc", str2 = "ad"
#Output: true
#Explanation: Select index 2 in str1.
#Increment str1[2] to become 'd'. 
#Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.


#my own solution using python3:

#annoying ass edge cases

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz"
        d = dict()
        for i in range(26):
            d[letters[i]] = i 
        one = deque(str1)
        seen = set(one)
        differencetwo = set(str2).difference(set(str1))
        print(differencetwo)
        differenceone = set(str1).difference(set(str2))
        print(differenceone)
        if len(differenceone) == 1 and len(differencetwo) == 1:
            if list(differenceone)[0] != "z":
                if d[list(differenceone)[0]] > d[list(differencetwo)[0]]:
                    return False

        for two in str2:
            if two in seen:
                seen.discard(one.popleft())
            else:
                flag = False
                for o in one:
                    if o == "z" and two == "a":
                        seen.discard(one.popleft())
                        flag = True
                        break
                    first = d[o]
                    second = d[two]
                    diff = abs(first - second)
                    if diff <= 1 and second >= first:
                        seen.discard(one.popleft())
                        flag = True
                        break
                if not flag:
                    return False
        return True
