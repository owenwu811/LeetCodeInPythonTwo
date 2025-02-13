

#3038
#easy

#You are given an array of integers nums. Consider the following operation:

#Delete the first two elements nums and define the score of the operation as the sum of these two elements.
#You can perform this operation until nums contains fewer than two elements. Additionally, the same score must be achieved in all operations.

#Return the maximum number of operations you can perform.

 

#Example 1:

#Input: nums = [3,2,1,4,5]

#Output: 2

#Explanation:

#We can perform the first operation with the score 3 + 2 = 5. After this operation, nums = [1,4,5].
#We can perform the second operation as its score is 4 + 1 = 5, the same as the previous operation. After this operation, nums = [5].
#As there are fewer than two elements, we can't perform more operations.


#my own solution using python3:

#just use a deque and pop from the front 2 times each turn, and check if the sum is equal to the previous sum

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        cur = []
        turns = 0
        nums = deque(nums)
        while len(nums) > 1:
            now = 0
            now += nums.popleft()
            now += nums.popleft()
            if cur:
                if now != cur[-1]:
                    return turns
            cur.append(now)
            turns += 1
            print(cur)
        return turns
        
