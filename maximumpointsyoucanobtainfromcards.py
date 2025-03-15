
#1423
#medium

#There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

#In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

#Your score is the sum of the points of the cards you have taken.

#Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

#Example 1:

#Input: cardPoints = [1,2,3,4,5,6,1], k = 3
#Output: 12
#Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.


#my own solution after reading hints:

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = k
        res = 0
        size = len(cardPoints) - k
        tot = sum(cardPoints)
        res = 0
        p = list(itertools.accumulate(cardPoints))
        for i in range(len(cardPoints) - size + 1):
            #ss = p[i + size] - p[i]
            cur = cardPoints[i: i + size]
            #print(cur)
            if i <= 0:
                ss = p[i + size - 1]
            else:
                ss = p[i + size - 1] - p[i - 1]
            res = max(res, tot - ss)
        return res
