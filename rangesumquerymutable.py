#307
#medium

#Given an integer array nums, handle multiple queries of the following types:

#Update the value of an element in nums.
#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#Implement the NumArray class:

#NumArray(int[] nums) Initializes the object with the integer array nums.
#void update(int index, int val) Updates the value of nums[index] to be val.
#int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

#Example 1:

#Input
#["NumArray", "sumRange", "update", "sumRange"]
#[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
#Output
#[null, 9, null, 8]



#correct python3 solution (could not solve without TLE):

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = nums
        self.tot = sum(self.n)

    def update(self, index: int, val: int) -> None:
        self.tot -= self.n[index]
        self.tot += val

        self.n[index] = val

        
        

    def sumRange(self, left: int, right: int) -> int:
        return self.tot - (sum(self.n[:left]) + sum(self.n[right + 1:]))


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
