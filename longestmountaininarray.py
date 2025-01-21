#845
#medium


#You may recall that an array arr is a mountain array if and only if:

#arr.length >= 3
#There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

#Input: arr = [2,1,4,7,3,2,5]
#Output: 5
#Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

#my own solution using python3:

#expand outwards from each index

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            cur = arr[i]
            left = i - 1
            right = i + 1
            if left >= 0 and right < len(arr):
                if arr[left] < cur > arr[right]:
                    while left >= 0 and arr[left] < cur and arr[left] < arr[left + 1]:
                        left -= 1
                    while right < len(arr) and arr[right] < cur and arr[right] < arr[right - 1]:
                        right += 1
                    left += 1
                    right -= 1
                    print(left, right)
                    res = max(res, right - left + 1)
                    
        return res
