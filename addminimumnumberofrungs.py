#1936
#medium

#You are given a strictly increasing integer array rungs that represents the height of rungs on a ladder. You are currently on the floor at height 0, and you want to reach the last rung.

#You are also given an integer dist. You can only climb to the next highest rung if the distance between where you are currently at (the floor or on a rung) and the next rung is at most dist. You are able to insert rungs at any positive integer height if a rung is not already there.

#Return the minimum number of rungs that must be added to the ladder in order for you to climb to the last rung.

 

#Example 1:

#Input: rungs = [1,3,5,10], dist = 2
#Output: 2
#Explanation:
#You currently cannot reach the last rung.
#Add rungs at heights 7 and 8 to climb this ladder. 
#The ladder will now have rungs at [1,3,5,7,8,10].


#my own solution using python3:

#make sure to take care of edge cases where the difference in gap is odd

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = math.ceil(abs((dist - rungs[0]) // dist))
        print(res)
        for i in range(1, len(rungs)):
            diff = rungs[i] - rungs[i - 1]
            if diff > dist:
                if diff % dist != 0:

                    res += math.ceil((diff - dist) // dist + 1)
                else:
                    res += math.ceil((diff - dist) // dist)
        return res
