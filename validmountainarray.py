#941
#easy

#Given an array of integers arr, return true if and only if it is a valid mountain array.

#Recall that arr is a mountain array if and only if:

#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

#Input: arr = [2,1]
#Output: false

#my own solution using python3:

#just simulate each of the conditions asked

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr == sorted(arr) or arr == sorted(arr, reverse=True):
            return False
        if len(arr) >= 3:
            for i in range(1, len(arr) - 1):
                if arr[i] == arr[i - 1] or arr[i - 1] > arr[i] < arr[i + 1]:
                    return False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
        return True
