
#2964
#medium

#Given a 0-indexed integer array nums and an integer d, return the number of triplets (i, j, k) such that i < j < k and (nums[i] + nums[j] + nums[k]) % d == 0.
 

#Example 1:

#Input: nums = [3,3,4,7,8], d = 5
#Output: 3
#Explanation: The triplets which are divisible by 5 are: (0, 1, 2), (0, 2, 4), (1, 2, 4).
#It can be shown that no other triplet is divisible by 5. Hence, the answer is 3.


#correct python3 solution (could not solve):

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        
        dd = defaultdict(list)
        for i, n in enumerate(nums):
            dd[n % d].append(i)

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ps_mod = (nums[i] + nums[j]) % d
                target_mod = (-ps_mod) % d
                if target_mod in dd:
                    idx_list = dd[target_mod]
                    pos = bisect_right(idx_list, j)
                    res += len(idx_list) - pos
        return res
