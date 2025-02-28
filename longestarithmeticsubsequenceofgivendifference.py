
#1218
#medium

#Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

#A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: arr = [1,2,3,4], difference = 1
#Output: 4
#Explanation: The longest arithmetic subsequence is [1,2,3,4].



#my own solution using python3:

#use a hashmap to keep track of the current values: indexes from the left up to i

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 0
        d = defaultdict(list)
        dp = [1] * len(arr)
        for i, a in enumerate(arr):
            d[a].append(i)
        for i in range(len(arr) -1, -1, -1):
            cur = arr[i]
            d[cur].pop()
            if not d[cur]:
                del d[cur]
            diff = cur - difference
            for a in d[diff]:
                dp[a] = dp[i] + 1
        return max(dp)
            
