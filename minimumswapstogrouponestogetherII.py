
#2134
#medium

#A swap is defined as taking two distinct positions in an array and swapping the values in them.

#A circular array is defined as an array where we consider the first element and the last element to be adjacent.

#Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 

#Example 1:

#Input: nums = [0,1,0,1,1,0,0]
#Output: 1
#Explanation: Here are a few of the ways to group all the 1's together:
#[0,0,1,1,1,0,0] using 1 swap.
#[0,1,1,1,0,0,0] using 1 swap.
#[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
#There is no way to group all 1's together with 0 swaps.
#Thus, the minimum number of swaps required is 1.


#my own solution using python3 after reading hint:

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        freq = nums.count(1)
        #print(freq)
        nums.extend(nums[:freq])
        n = len(nums)
        ans = float('inf')
        c = Counter(nums[:freq])
        for i in range(len(nums) - freq + 1):
            #print(i, i + freq)
            #print(c)
            ans = min(ans, c[0])
           # cur = nums[i: i + freq]
            #print(cur)
            if i + freq < n:
                c[nums[i + freq]] += 1
            if i >= 0 and i < n:
                c[nums[i]] -= 1
                if c[nums[i]] <= 0:
                    del c[nums[i]]
            #print(c, cur)
            #ans = min(ans, cur.count(0))
        return ans
