
#2379
#easy

#You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

#You are also given an integer k, which is the desired number of consecutive black blocks.

#In one operation, you can recolor a white block such that it becomes a black block.

#Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

#Example 1:

#Input: blocks = "WBBWWBBWBW", k = 7
#Output: 3
#Explanation:
#One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
#so that blocks = "BBBBBBBWBW". 
#It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
#Therefore, we return 3.



#my own solution using python3:

#slide the window over size k and get the fewest number of Ws in each window as your solution

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        size = k
        res = float('inf')
        for i in range(len(blocks) - size + 1):
            substr = blocks[i: i + size]
            print(substr)
            res = min(res, substr.count("W"))
        return res
