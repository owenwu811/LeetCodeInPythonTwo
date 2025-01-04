
#2138
#easy

#A string s can be partitioned into groups of size k using the following procedure:

#The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each character can be a part of exactly one group.
#For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
#Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

#Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.

 

#Example 1:

#Input: s = "abcdefghi", k = 3, fill = "x"
#Output: ["abc","def","ghi"]
#Explanation:
#The first 3 characters "abc" form the first group.
#The next 3 characters "def" form the second group.
#The last 3 characters "ghi" form the third group.
#Since all groups can be completely filled by characters from the string, we do not need to use fill.
#Thus, the groups formed are "abc", "def", and "ghi".



#my own solution using python3:

#watch out for edge case where k is bigger than length of s - otherwise, use a sliding window of size k and fill in any leftovers with whatever the fill variable is 

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) < k:
            ans = s + (fill * (k - len(s)))
            print(ans)
            return [ans]
        res = []
        cur = 0
        for i in range(0, len(s) - k + 1, k):
            cur = i + k - 1
            substr = s[i: i + k]
            print(substr)
            res.append("".join(substr))
        print(cur)
        #print(i + k - 1, len(s) - 1)
        diff = cur
        end = len(s) - 1
        leftover = s[diff + 1: end + 1]
        print(leftover)
        while len(leftover) < k:
            leftover += fill
        print(leftover)
        if len(set(leftover)) > 1:
            res.append(leftover)
        return res
