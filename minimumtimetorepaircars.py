
#2594
#medium

#You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

#You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

#Return the minimum time taken to repair all the cars.

#Note: All the mechanics can repair the cars simultaneously.

 

#Example 1:

#Input: ranks = [4,2,3,1], cars = 10
#Output: 16

#correct python3 solution (could not solve):

#question lacks clarity and enough information to solve without reading authors' mind:

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, max(ranks) * (cars ** 2)
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for rank in ranks:
                cur += floor(sqrt(mid // rank))
            if cur >= cars:
                r = mid - 1
            else:
                l = mid + 1
        return l
