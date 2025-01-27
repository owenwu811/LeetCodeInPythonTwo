#2256
#medium

#You are given a 0-indexed integer array nums of length n.

#The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

#Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

#Note:

#The absolute difference of two numbers is the absolute value of their difference.
#The average of n elements is the sum of the n elements divided (integer division) by n.
#The average of 0 elements is considered to be 0.
 

#Example 1:

#Input: nums = [2,5,3,9,5,3]
#Output: 3
#Explanation:
#- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
#- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
#- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
#- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
#- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
#- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
#The average difference of index 3 is the minimum average difference so return 3.


#my own solution using python3:

#instead of recalculating the sums, just subtract the left total sum, so keep track of cumulative sum from left and right in opposite directions 

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        #[2] > length 1
        #[5, 3, 9, 5, 3] > length 5
        tot = sum(nums)
        #[2,5,3,9,5,3]
        #[2, 5], [3, 9, 5, 3]
        #[2, 5, 3], [9, 5, 3]


        ans = []
        historical = float('inf')
        leftsum = 0
        tot = sum(nums)
        for i in range(len(nums)):
            tot -= nums[i]
            leftsum += nums[i]
            rightsum = tot
            leftval, rightval = i + 1, len(nums) - i - 1
            if rightval == 0:
                cur = abs(leftsum // leftval - (rightsum) - rightval)
            else:
                cur = abs(leftsum // leftval - (rightsum) // rightval)
            if historical > cur:
                historical = cur
                print(i, "i")
                ans.append(i)
            print(cur, "cur")
           # 2 25
           # 1 5
        return ans[-1]
