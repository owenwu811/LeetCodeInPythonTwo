#3079
#easy

#You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

#Return the sum of encrypted elements.

 

#Example 1:

#Input: nums = [1,2,3]

#Output: 6

#Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.


#my own solution using python3:

#you just take the biggest element of each element and multiply it by the length of the element and add together at the end

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = []
        for i, n in enumerate(nums):
            nums[i] = str(n)
        for i in range(len(nums)):
            biggest = 0
            for j in range(len(nums[i])):
                biggest = max(biggest, int(nums[i][j]))
            print(biggest)
            res.append(str(biggest) * len(nums[i]))
        print(res)
        ans = 0
        for r in res:
            ans += int(r)
        return ans
