
#3208
#medium

#There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

#colors[i] == 0 means that tile i is red.
#colors[i] == 1 means that tile i is blue.
#An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

#Return the number of alternating groups.

#Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

#Example 1:

#Input: colors = [0,1,0,1,0], k = 3

#Output: 3


#my own solution using python3:

#use fixed size sliding window

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        #colors.append(colors)
        #ans = []
        colors.extend(colors[:k - 1])
        before = ["g"]
        for i in range(1, len(colors) - 1):
            if colors[i] == colors[i - 1] or colors[i] == colors[i + 1]:
                before.append("b")
            else:
                before.append("g")
        before.append("g")
        c = Counter(before[:k - 1])
        for i in range(len(colors) - k + 1):
            c[before[i]] -= 1
            if c[before[i]] == 0:
                del c[before[i]]
            if not c["b"]:
                ans += 1
            c[before[i + k - 1]] += 1
            #print(now, c)
            #if "b" not in now:
            #    ans += 1
        return ans
