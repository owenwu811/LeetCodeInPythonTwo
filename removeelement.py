#27
#easy

#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.


 

#Example 1:

#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 2.
#It does not matter what you leave beyond the returned k (hence they are underscores).


#my own solution using python3:

#just create a new array with all elements from input excluding val and then reassign the input list without returning anything

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #[3, 2, 2, 3]
        #[3, 2]
        #[2]

        h = []
        print(nums)
        for n in nums:
            if n == val:
                continue
            h.append(n)
        print(h)
        nums[:] = h
