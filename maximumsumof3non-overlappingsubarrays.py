#689
#hard

#Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

#Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

#Example 1:

#Input: nums = [1,2,1,2,6,7,5,1], k = 2
#Output: [0,3,5]
#Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
#We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically smaller.
#Example 2:

#Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
#Output: [0,2,4]


#my own solution using python3:

#do one iteration to calculate the maximum possible sum and another to find the lowest indicies that satisfy the requirements, and then do prefix sums to avoid tle when preprocessing the data

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        cur = []
        p = list(itertools.accumulate(nums))
        for i in range(len(nums) - k + 1):
            if i <= 0:
                now = p[i + k - 1]
            else: 
                now = p[i + k - 1] - p[i - 1]
            cur.append(now)
        sl = SortedList()
        ans = 0
        for i in range(k, len(cur) - k):
            #print(cur[:i - k + 1], cur[i], cur[i + k:])
            bl = max(cur[:i - k + 1])
            br = max(cur[i + k:])
            ans = max(ans, bl + cur[i] + br)
        for i in range(k, len(cur) - k):
            #print(cur[:i - k + 1], cur[i], cur[i + k:])
            bl = max(cur[:i - k + 1])
            br = max(cur[i + k:])
            if bl + cur[i] + br == ans:
                #print(br)
                for j in range(i + k, len(cur)):
                    if cur[j] == br:
                        #print(j)
                        li = cur[:i - k + 1].index(bl)
                        sl.add((li, i, j))
                        break


                #print(cur[:i - k + 1].index(bl), i, cur.index(br))
                #ri = max(cur.index(br), k * 2)
                #sl.add((li, i))
        return sl[0]
