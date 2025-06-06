
#506
#easy

#You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

#The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

#The 1st place athlete's rank is "Gold Medal".
#The 2nd place athlete's rank is "Silver Medal".
#The 3rd place athlete's rank is "Bronze Medal".
#For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
#Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

#Example 1:

#Input: score = [5,4,3,2,1]
#Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
#Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].



#my own solution using python3 on 6/5/25 (originally solved on November, 2023) but didn't make the file:

#simulate the instructions by mapping the indexes to values and sorting the values and finding their original index locations

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [0] * len(score)
        cnt = 0
        sl = SortedList()
        d = dict()
        for i, s in enumerate(score):
            sl.add((s, i))
            d[s] = i
        #print(sl)
        cnt = 1
        d = ["Bronze Medal", "Silver Medal", "Gold Medal"]

        for a in sl[::-1]:
            #print(a[0])
            idx = score.index(a[0])
            if d:
                res[idx] = d.pop()
            else:
                res[idx] = str(cnt)

            cnt += 1
        print(res)
        return res
