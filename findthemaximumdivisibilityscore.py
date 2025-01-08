
#2644
#easy

#You are given two integer arrays nums and divisors.

#The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].

#Return the integer divisors[i] with the maximum divisibility score. If multiple integers have the maximum score, return the smallest one.

 

#Example 1:

#Input: nums = [2,9,15,50], divisors = [5,3,7,2]

#Output: 2


#my own solution using python3:

#follow the instructions

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        myd = dict()
        for d in divisors:
            cur = 0
            for n in nums:
                if n % d == 0:
                    cur += 1
            print(cur)
            myd[d] = cur
        print(myd)
        print(max(myd.values()))
        smallest = float('inf')
        for k in myd:
            if myd[k] == max(myd.values()):
                smallest = min(smallest, k)
        return smallest
