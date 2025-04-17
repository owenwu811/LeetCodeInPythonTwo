#3206
#easy

#There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

#colors[i] == 0 means that tile i is red.
#colors[i] == 1 means that tile i is blue.
#Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

#Return the number of alternating groups.

#Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

#Example 1:

#Input: colors = [1,1,1]


#my own solution using python3:

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        colors.extend(colors[:2])
        for i in range(len(colors) - 2):
            cur = colors[i: i + 3]
            print(cur)
            flag = True
            for i in range(1, len(cur) - 1):
                if cur[i] == cur[i - 1] or cur[i] == cur[i + 1]:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans
