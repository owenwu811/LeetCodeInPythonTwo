#2300
#medium

#You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

#You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

#Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

#Example 1:

#Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
#Output: [4,0,3]
#Explanation:
#- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
#- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
#- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
#Thus, [4,0,3] is returned.


#my own solution using python3:

#you know that you want to find the smallest number that, when multiplied, is atleast greater than or equal to, so we can sort potions to find this pivot point, and we find this pivot point using binary search

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for s in spells:
            if s * potions[-1] < success:
                res.append(0)
                continue
            l, r = 0, len(potions) - 1
            cur = []
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * s >= success:
                    cur.append(mid)
                    r = mid - 1
                else:
                    l = mid + 1
            print(cur)
            res.append(len(potions) - min(cur))

        return res
