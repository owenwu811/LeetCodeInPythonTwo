
#2031
#Medium

#You are given a binary array nums containing only the integers 0 and 1. Return the number of subarrays in nums that have more 1's than 0's. Since the answer may be very large, return it modulo 109 + 7.

#A subarray is a contiguous sequence of elements within an array.



#could not solve:

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        t = []
        for i, n in enumerate(nums):
            if n > 0:
                t.append(1)
            else:
                t.append(-1)
        print(t)
        ss = 0
        res = 0
        s = SortedList([0])
        for i, n in enumerate(t):
            ss += n
            res += bisect_left(s, ss)
            res = res % ((10 ** 9) + 7)
            s.add(ss)
        return res % ((10 ** 9) + 7)
