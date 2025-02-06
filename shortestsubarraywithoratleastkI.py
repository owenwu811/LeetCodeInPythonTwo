#3095
#easy

#You are given an array nums of non-negative integers and an integer k.

#An array is called special if the bitwise OR of all of its elements is at least k.

#Return the length of the shortest special non-empty 
#subarray
# of nums, or return -1 if no special subarray exists.

#my own solution using python3:

#Just brute force it

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                cur = subarr[0]
                for a in subarr[1:]:
                    cur = cur | a
                print(cur)
                if cur >= k:
                    res = min(res, len(subarr))
        if res == float('inf'):
            return -1
        return res
