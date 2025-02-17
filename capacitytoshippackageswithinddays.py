#1011
#medium

#A conveyor belt has packages that must be shipped from one port to another within days days.

#The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

#Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

#Example 1:

#Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
#Output: 15
#Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
#1st day: 1, 2, 3, 4, 5
#2nd day: 6, 7
#3rd day: 8
#4th day: 9
#5th day: 10



#my own solution after looking at another solution to understand what the question is even asking (they should improve the explanation):

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = float('inf')
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            cap = mid
            cur = 0
            dt = 1
            for w in weights:
                if cur + w <= cap:
                    cur += w
                else:
                    dt += 1
                    cur = w
            if dt <= days:
                res = min(res, cap)
                r = mid - 1
            else:
                l = mid + 1
        return res
