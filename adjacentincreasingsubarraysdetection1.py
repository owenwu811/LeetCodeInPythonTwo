#3349
#easy

#Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

#Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
#The subarrays must be adjacent, meaning b = a + k.
#Return true if it is possible to find two such subarrays, and false otherwise.

 

#Example 1:

#Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

#Output: true

#Explanation:

#The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
#The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
#These two subarrays are adjacent, so the result is true.


#my own solution using python3:

#Just brute force

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        

        d = dict()

        for i in range(len(nums)):
            subarr = nums[i: i + k]
            d[i] = subarr
        #print(d)
        for kk in d:
            #print(kk)
            if kk + k in d:
                print(d[kk], d[kk + k])
                if len(d[kk]) == len(d[kk + k]):
                    flag = True
                    for i in range(1, len(d[kk])):
                        if d[kk][i - 1] >= d[kk][i]:
                            flag = False
                    for i in range(1, len(d[kk + k])):
                        if d[kk + k][i - 1] >= d[kk + k][i]:
                            flag = False
                    if flag:
                        return True
        return False
                
