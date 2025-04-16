
#769
#medium

#You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

#We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

#Return the largest number of chunks we can make to sort the array.

 

#Example 1:

#Input: arr = [4,3,2,1,0]
#Output: 1
#Explanation:
#Splitting into two or more chunks will not return the required result.
#For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.


#my own solution using python3 after reading comment in disucss:

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        biggest = float('-inf')
        ans = 0
        for i, a in enumerate(arr):
            biggest = max(biggest, a)
            if i == biggest:
                print(i)
                ans += 1
        return ans
