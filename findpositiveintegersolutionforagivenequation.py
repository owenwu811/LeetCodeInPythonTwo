#1237
#medium

#Example 1:

#Input: function_id = 1, z = 5
#Output: [[1,4],[2,3],[3,2],[4,1]]
#Explanation: The hidden formula for function_id = 1 is f(x, y) = x + y.
#The following positive integer values of x and y make f(x, y) equal to 5:
#x=1, y=4 -> f(1, 4) = 1 + 4 = 5.
#x=2, y=3 -> f(2, 3) = 2 + 3 = 5.
#x=3, y=2 -> f(3, 2) = 3 + 2 = 5.
#x=4, y=1 -> f(4, 1) = 4 + 1 = 5.



#my own solution using python3:

#just use brute force

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        #print(customfunction)
        for i in range(1, 1001):
            for j in range(1, 1001):
                a = customfunction.f(i, j)
                if a == z:
                    if [i, j] not in res:
                        res.append([i, j])
                    #if [j, i] not in res:
                    #    res.append([j, i])
        return res
