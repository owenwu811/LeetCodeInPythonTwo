#2760
#easy

#You are given a 0-indexed integer array nums and an integer threshold.

#Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length) that satisfies the following conditions:

#nums[l] % 2 == 0
#For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
#For all indices i in the range [l, r], nums[i] <= threshold
#Return an integer denoting the length of the longest such subarray.

#Note: A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [3,2,5,4], threshold = 5
#Output: 3
#Explanation: In this example, we can select the subarray that starts at l = 1 and ends at r = 3 => [2,5,4]. This subarray satisfies the conditions.
#Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.


#my own solution using python3:

#check each of the conditions mentioned using brute force

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                if subarr[0] % 2 == 0:
                    flag = True
                    for a in range(1, len(subarr)):
                        if subarr[a] % 2 == subarr[a - 1] % 2:
                            flag = False
                            break
                    for b in range(len(subarr)):
                        if subarr[b] > threshold:
                            flag = False
                            break

                    if flag:
                        res = max(res, len(subarr))
        return res
