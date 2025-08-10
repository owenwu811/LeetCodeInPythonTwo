#2357
#easy

#You are given a non-negative integer array nums. In one operation, you must:

#Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
#Subtract x from every positive element in nums.
#Return the minimum number of operations to make every element in nums equal to 0.

 

#Example 1:

#Input: nums = [1,5,0,3,5]
#Output: 3
#Explanation:
#In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
#In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
#In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

#my own solution using python3:

#use a sortedlist to get the smallest element and count the turns by simulating the instructions

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sl = SortedList(nums)
        ans = 0
        while len(set(sl)) > 1 or sl[0] > 0:
            bl = bisect_left(sl, 1)
            print(sl, bl)
            if bl < len(sl):
                val = sl[bl]
                for a in sl:
                    if a > 0:
                        diff = a - val
                        sl.discard(a)
                        sl.add(diff)
                ans += 1
        return ans
