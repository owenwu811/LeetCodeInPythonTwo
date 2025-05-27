
#1104
#medium

#You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

#The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

#Return the maximum score of a pair of sightseeing spots.

 

#Example 1:

#Input: values = [8,1,5,2,6]
#Output: 11
#Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
#Example 2:

#Input: values = [1,2]
#Output: 2


#my own solution using python3:

#experiment with the indicies and values

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = []
        for i, v in enumerate(values):
            cur.append(v - i)
        ans = 0
        sl = SortedList(cur)
        for i in range(len(values) - 1):
            sl.discard(values[i] - i)
            ans = max(ans, values[i] + sl[-1] + i)
        return ans

