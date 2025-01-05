#822
#medium

#You are given two 0-indexed integer arrays fronts and backs of length n, where the ith card has the positive integer fronts[i] printed on the front and backs[i] printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

#After flipping the cards, an integer is considered good if it is facing down on some card and not facing up on any card.

#Return the minimum possible good integer after flipping the cards. If there are no good integers, return 0.

 

#Example 1:

#Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
#Output: 2
#Explanation:
#If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
#2 is the minimum good integer as it appears facing down but not facing up.
#It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.


#my own solution using python3:

#took a lot of trial and error to figure out what this question is asking

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        res = []
        bad = []
        for i, f in enumerate(fronts):
            if fronts[i] != backs[i]:
                res.append(fronts[i])
                res.append(backs[i])
            else:
                if fronts[i] in res:
                    res.remove(fronts[i])
                if backs[i] in res:
                    res.remove(backs[i])
                bad.append(fronts[i])
                bad.append(backs[i])
        print(res, bad)
        ans = float('inf')
        for r in res:
            if r not in bad:
                ans = min(ans, r)
        if ans == float('inf'):
            return 0
        return ans
