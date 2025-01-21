#978
#medium


#Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

#A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

#More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

#For i <= k < j:
#arr[k] > arr[k + 1] when k is odd, and
#arr[k] < arr[k + 1] when k is even.
#Or, for i <= k < j:
#arr[k] > arr[k + 1] when k is even, and
#arr[k] < arr[k + 1] when k is odd.


#correct python3 solution (could not solve):

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        size = len(arr)
        increasing, decreasing, res = 1, 1, 1
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                decreasing = increasing + 1
                increasing = 1
            elif arr[i - 1] < arr[i]:
                increasing = decreasing + 1
                decreasing = 1
            else:
                increasing = decreasing = 1
            res = max(res, increasing, decreasing)
        return res
