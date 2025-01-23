#1578
#medium

#Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

#Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

#Return the minimum time Bob needs to make the rope colorful.

#Input: colors = "abaac", neededTime = [1,2,3,4,5]
#Output: 3
#Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
#Bob can remove the blue balloon at index 2. This takes 3 seconds.
#There are no longer two consecutive balloons of the same color. Total time = 3.


#my own solution using python3:

#get rid of the largest value in each same letter sequence

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tot = SortedList(neededTime.copy())
        i = 0
        j = 0
        seen = set(tot)
        while i < len(colors):
            r = SortedList()
            print(colors[i])
            while j < len(colors):
                if colors[j] == colors[i]:
                    r.add(neededTime[j])
                else:
                    break
                j += 1
            i = j
            print(j)
            print(r)
            if r[-1] in tot:
                tot.remove(r[-1])
        return sum(tot)
