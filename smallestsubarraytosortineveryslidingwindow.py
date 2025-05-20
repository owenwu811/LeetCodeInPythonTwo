
#3555
#medium

#You are given an integer array nums and an integer k.

#For each contiguous subarray of length k, determine the minimum length of a continuous segment that must be sorted so that the entire window becomes non‑decreasing; if the window is already sorted, its required length is zero.

#Return an array of length n − k + 1 where each element corresponds to the answer for its window.

 

#Example 1:

#Input: nums = [1,3,2,4,5], k = 3

#Output: [2,2,0]

#Explanation:

#nums[0...2] = [1, 3, 2]. Sort [3, 2] to get [1, 2, 3], the answer is 2.
#nums[1...3] = [3, 2, 4]. Sort [3, 2] to get [2, 3, 4], the answer is 2.
#nums[2...4] = [2, 4, 5] is already sorted, so the answer is 0.

#my own solution using python3:

#find the sorted vs. current subarray and the leftmost and rightmost non matching values aka out of place values, and add one to it assuming both exist

class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            subarr = nums[i: i + k]
            key = sorted(subarr)
            #print(subarr)
            #print(key)
            cnt = 0
            low = float('inf')
            high = float('-inf')
            for j in range(len(subarr)):
                if subarr[j] != key[j]:
                    low = min(low, j)
                    high = max(high, j)
                    cnt += 1
            print(low, high)
            if low == float('inf') or high == float('-inf'):
                ans.append(0)
            else:
                ans.append(high - low + 1)
        return ans
