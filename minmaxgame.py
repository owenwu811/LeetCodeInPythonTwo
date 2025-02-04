#2293
#easy

#You are given a 0-indexed integer array nums whose length is a power of 2.

#Apply the following algorithm on nums:

#Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
#For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
#For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
#Replace the array nums with newNums.
#Repeat the entire process starting from step 1.
#Return the last number that remains in nums after applying the algorithm.


#my own solution using python3:

#just follow the steps

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            new = [0] * (len(nums) // 2)
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    new[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    new[i] = max(nums[2 * i], nums[2 * i + 1])
            nums[:] = new
        return nums[-1]
