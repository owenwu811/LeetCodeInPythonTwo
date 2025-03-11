
#1343
#medium

#Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

#Example 1:

#Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
#Output: 3
#Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold)


#my own solution using python3 on 3/11/25 (originally solved august 2024 but forgot to upload file):

#use prefix sums since you know fixed size sliding window

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        size = k
        res = 0
        a = len(arr)
        p = list(itertools.accumulate(arr))
        #[1, 2, 3, 4, 5]
        #[1, 3, 6]
        for i in range(a - size + 1):
            if i <= 0:
                cur = p[i + size - 1]
            else:
                cur = p[i + size - 1] - p[i - 1]
            if cur // k >= threshold: res += 1
        return res
