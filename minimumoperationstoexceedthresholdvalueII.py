#3066
#medium

#You are given a 0-indexed integer array nums, and an integer k.

#You are allowed to perform some operations on nums, where in a single operation, you can:

#Select the two smallest integers x and y from nums.
#Remove x and y from nums.
#Insert (min(x, y) * 2 + max(x, y)) at any position in the array.
#Note that you can only apply the described operation if nums contains at least two elements.

#Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

 

#Example 1:

#Input: nums = [2,11,10,1,3], k = 10

#Output: 2

#Explanation:

#In the first operation, we remove elements 1 and 2, then add 1 * 2 + 2 to nums. nums becomes equal to [4, 11, 10, 3].
#In the second operation, we remove elements 3 and 4, then add 3 * 2 + 4 to nums. nums becomes equal to [10, 11, 10].
#At this stage, all the elements of nums are greater than or equal to 10 so we can stop. 

#It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.




#my own solution using python3:

#literally just follow the instructions - you can use a heap or a SortedList() - they do the same thing

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        s = SortedList(nums)
        while len(s) >= 2:
            #print(s)
            if s[0] >= k:
                return res
            a = s[0]
            del s[0]
            b = s[0]
            del s[0]
            print(a, b)
            newval = min(a, b) * 2 + max(a, b)
            s.add(newval)
            res += 1
        return res
