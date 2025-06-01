#5/31/25 contest question 1

#You are given an integer array nums containing distinct positive integers and an integer target.

#Determine if you can partition nums into two non-empty disjoint subsets, with each element belonging to exactly one subset, such that the product of the elements in each subset is equal to target.

#Return true if such a partition exists and false otherwise.

#A subset of an array is a selection of elements of the array.
 

#Example 1:

#Input: nums = [3,1,6,8,4], target = 24

#Output: true

#Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true.


#my own solution using python3:

#just find all combinations of all sizes since the input is small

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        cur = []
        for i in range(1, len(nums) + 1):
            for a in combinations(nums, i):
                if prod(a) == target:
                    print(a, cur)
                    for c in cur:
                        now = set(c)
                        now.update(set(a))
                        print(now)
                        if set(now) == set(nums):
                        #if len(a) + len(a) == len(nums):
                            return True
                    cur.append(a)
        return False
                    
