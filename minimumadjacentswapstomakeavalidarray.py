
#2340
#medium

#You are given a 0-indexed integer array nums.

#Swaps of adjacent elements are able to be performed on nums.

#A valid array meets the following conditions:

#The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
#The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
#Return the minimum swaps required to make nums a valid array.

 

#Example 1:

#Input: nums = [3,4,5,5,3,1]
#Output: 6
#Explanation: Perform the following swaps:
#- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
#- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
#- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
#- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
#- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
#- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
#It can be shown that 6 swaps is the minimum swaps required to make a valid array.


#my own solution using python3:

#find the smallest distance of smallest index to right and opposite to left and take care of some edge cases if they don't cross

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        smallest, largest = min(nums), max(nums)
        res = 0
        smalldist, largedist = [], []
        for i in range(len(nums)):
            if nums[i] == smallest:
                smalldist.append(i)
            if nums[i] == largest:
                largedist.append(i)
        print(smalldist, largedist, "small, large")
        a = float('inf')
        for s in smalldist:
            print(s, 0)
            a = min(a, abs(s - 0))
        b = float('inf')
        for l in largedist:
            print(l, len(nums) - 1)
            b = min(b, abs(l - (len(nums) - 1)))
        print(a, b) 
        if min(smalldist) > max(largedist):
            return a + b - 1
        return a + b
