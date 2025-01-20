#1151
#medium

#Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

#Example 1:

#Input: data = [1,0,1,0,1]
#Output: 1
#Explanation: There are 3 ways to group all 1's together:
#[1,1,1,0,0] using 1 swap.
#[0,1,1,1,0] using 2 swaps.
#[0,0,1,1,1] using 1 swap.
#The minimum is 1.


#my own solution using python3:

#sliding window of frequency of 1s and find the smallest frequency of 0s in any subarray

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        h = Counter(data)
        size = h[1]
        if size <= 1:
            return 0
        res = float('inf')
        c = Counter(data[:size])
        res = min(res, c[0])
        l = 0
        for i in range(1, len(data) - size + 1):
            c[data[l]] -= 1
            c[data[i + size - 1]] += 1
            res = min(res, c[0])
            l += 1
        return res
