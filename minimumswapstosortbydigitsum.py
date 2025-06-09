#3551
#medium

#You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

#Return the minimum number of swaps required to rearrange nums into this sorted order.

#A swap is defined as exchanging the values at two distinct positions in the array.

 

#Example 1:

#Input: nums = [37,100]

#Output: 1

#Explanation:

#Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
#Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
#Thus, the minimum number of swaps required to rearrange nums is 1.


#my own solution using python3:

#group by the sum using a heap before running selection sort using a dictionary

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sl = SortedList()
        ans = 0
        for n in nums:
            cur = 0
            for y in str(n):
                cur += int(y)
            sl.add((cur, n))
        now = []
        for s in sl:
            now.append(s[1])
        #print(nums, now)
        #[18, 43, 34, 16] nums

        #[16, 34, 43, 18] now

        #{18: 0}
        #{16: 3}

        #{18:3}
        #{16:0}
        d = dict()
        for i, n in enumerate(nums):
            d[n] = i
        for i in range(len(nums)):
            if now[i] != nums[i]:
                target = now[i]
                if target in d:
                    ti = d[target]
                    left = nums[i]
                    #print(left, d[left])
                    right = nums[ti]
                    #print(right, d[right])
                    nums[i], nums[ti] = nums[ti], nums[i]
                    #print(nums)
                    #print(left, i)
                    d[left] = ti
                    d[right] = i
                    #print(left, d[left])
                    #print(right, d[right])
                    ans += 1
                    #break
            del d[nums[i]]
        return ans

