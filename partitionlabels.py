
#763
#medium

#You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

#Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

#Return a list of integers representing the size of these parts.

 

#Example 1:

#Input: s = "ababcbacadefegdehijhklij"
#Output: [9,7,8]
#Explanation:
#The partition is "ababcbaca", "defegde", "hijhklij".
#This is a partition so that each letter appears in at most one part.
#A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

#my own solution using python3:

#use merge intervals with the values of the dictionary's keys

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        cur = []
        for k in d:
            cur.append(d[k])
        new = []
        for i in range(len(cur)):
            if not new:
                new.append(cur[i])
            if cur[i][0] > new[-1][-1]:
                new.append(cur[i])
            for j in range(i + 1, len(cur)):
                if cur[j][0] <= new[-1][-1]:
                    new[-1][-1] = max(new[-1][-1], cur[j][-1])
                else:
                    #print(new, cur[j])
                    if cur[j] not in new and cur[j][0] > new[-1][-1]:
                        new.append(cur[j])
                    break
        print(new)
        ans = []
        for n in new:
            ans.append(n[-1] - n[0] + 1)
        return ans
                
