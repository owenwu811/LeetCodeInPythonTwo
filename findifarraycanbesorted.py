#3011
#medium

#You are given a 0-indexed array of positive integers nums.

#In one operation, you can swap any two adjacent elements if they have the same number of set bits. You are allowed to do this operation any number of times (including zero).

#Return true if you can sort the array in ascending order, else return false.

 

#Example 1:

#Input: nums = [8,4,2,30,15]
#Output: true
#Explanation: Let's look at the binary representation of every element. The numbers 2, 4, and 8 have one set bit each with binary representation "10", "100", and "1000" respectively. The numbers 15 and 30 have four set bits each with binary representation "1111" and "11110".


#my own solution using python3:

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        #[3, 16,  8, 4,2]
        #11 10000 1000 100 10

        for i in range(len(nums)):
            cur = bin(int(nums[i]))[2:]
            for j in range(i + 1, len(nums)):
                jj = bin(int(nums[j]))[2:]
                if nums[j] < nums[i] and jj.count("1") != cur.count("1"):
                    return False
            
            #if nums[i] < nums[i - 1] and prev.count("1") 
        return True
