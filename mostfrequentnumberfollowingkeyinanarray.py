
#2190
#easy

#You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

#For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

#0 <= i <= nums.length - 2,
#nums[i] == key and,
#nums[i + 1] == target.
#Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.

 

#Example 1:

#Input: nums = [1,100,200,1,100], key = 1
#Output: 100
#Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
#No other integers follow an occurrence of key, so we return 100.




#my own solution using python3:

#find the number that has highest frequency and appears one place to the right of key in the input array

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = defaultdict(int)
        for i in range(1, len(nums)):
            if nums[i - 1] == key:
                d[nums[i]] += 1
        print(d)
        t = max(d.values())
        for k in d:
            if d[k] == t:
                return k
