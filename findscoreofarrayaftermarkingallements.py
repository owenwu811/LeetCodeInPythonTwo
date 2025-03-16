#2593
#medium


#You are given an array nums consisting of positive integers.

#Starting with score = 0, apply the following algorithm:

#Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
#Add the value of the chosen integer to score.
#Mark the chosen element and its two adjacent elements if they exist.
#Repeat until all the array elements are marked.
#Return the score you get after applying the above algorithm.

 

#Example 1:

#Input: nums = [2,1,3,4,5,2]
#Output: 7
#Explanation: We mark the elements as follows:
#- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
#- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
#- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
#Our score is 1 + 2 + 4 = 7.


#this question makes literally no sense:

class Solution:
    def findScore(self, nums: List[int]) -> int:
        h = SortedList()
        d = dict()
        for i, n in enumerate(nums):
            h.add((n, i))

        res = 0
        seen = set()
        while h:
            val, idx = h[0][0], h[0][1]
            h.pop(0)
            if idx in seen:
                continue
            res += val
            seen.add(idx - 1)
            seen.add(idx + 1)
            
        return res
