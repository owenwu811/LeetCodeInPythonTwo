
#1029
#medium

#A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

#Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

#Example 1:

#Input: costs = [[10,20],[30,200],[400,50],[30,20]]
#Output: 110



#correct python3 solution (could not solve):

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        n = len(costs) // 2
        
        for i in range(n):
            total += costs[i][0]
        for i in range(n, len(costs)):
            total += costs[i][1]
        
        return total
