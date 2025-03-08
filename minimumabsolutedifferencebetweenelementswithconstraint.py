
#2817
#medium

#You are given a 0-indexed integer array nums and an integer x.

#Find the minimum absolute difference between two elements in the array that are at least x indices apart.

#In other words, find two indices i and j such that abs(i - j) >= x and abs(nums[i] - nums[j]) is minimized.

#Return an integer denoting the minimum absolute difference between two elements that are at least x indices apart.

 

#Example 1:

#Input: nums = [4,3,2,4], x = 2
#Output: 0
#Explanation: We can select nums[0] = 4 and nums[3] = 4. 
#They are at least 2 indices apart, and their absolute difference is the minimum, 0. 
#It can be shown that 0 is the optimal answer.


#my own solution using python3:

#use sorted list and bisect to carefully only get cur - x before and cur + x after in sorted order

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        res = float('inf')
        n = len(nums)
        before = SortedList()
        after = SortedList(nums[x:])
        print(before, after)
        for i in range(n):
            low = i - x
            high = i + x
            print(low, high)
            if low >= 0:
                print(low, "low")
                before.add(nums[low])
                l = bisect_left(before, nums[i])
                if l >= 0 and l < len(before):
                    res = min(res, abs(nums[i] - before[l]))
                if l - 1 >= 0:
                    res = min(res, abs(nums[i] - before[l - 1]))
            if high < n:
                print(high, "high")
                after.remove(nums[high])
                #after = sorted(nums[high:])
                r = bisect_left(after, nums[i])
                if r >= 0 and r < len(after):
                    res = min(res, abs(nums[i] - after[r]))
                if r + 1 < len(after):
                    res = min(res, abs(nums[i] - after[r + 1]))
                if r - 1 >= 0:
                    res = min(res, abs(nums[i] - after[r - 1]))
        return res
            #-2 0 2
           # -1 1 3
            #0 2 4
            #1 3 5

            
