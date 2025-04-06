
#1788
#hard

#There is a garden of n flowers, and each flower has an integer beauty value. The flowers are arranged in a line. You are given an integer array flowers of size n and each flowers[i] represents the beauty of the ith flower.

#A garden is valid if it meets these conditions:

#The garden has at least two flowers.
#The first and the last flower of the garden have the same beauty value.
#As the appointed gardener, you have the ability to remove any (possibly none) flowers from the garden. You want to remove flowers in a way that makes the remaining garden valid. The beauty of the garden is the sum of the beauty of all the remaining flowers.

#Return the maximum possible beauty of some valid garden after you have removed any (possibly none) flowers.

 

#Example 1:

#Input: flowers = [1,2,3,1,2]
#Output: 8
#Explanation: You can produce the valid garden [2,3,1,2] to have a total beauty of 2 + 3 + 1 + 2 = 8.


#my own solution using python3:

#use prefix sum to remove negatives of a subarray to avoid tle

class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        d = defaultdict(list)
        neg = []
        for i, f in enumerate(flowers):
            d[f].append(i)
            if f < 0:
                neg.append(i)
        p = list(itertools.accumulate(flowers))
        res = float('-inf')
        for k in d: 
            if len(d[k]) >= 2:
                low = d[k][0] 
                high = d[k][-1]
                if low <= 0:
                    cur = p[high]
                else:
                    cur = p[high] - p[low - 1]
                for n in neg:
                    if low + 1 <= n < high:
                        cur -= flowers[n]
                
                res = max(res, cur)
        return res
