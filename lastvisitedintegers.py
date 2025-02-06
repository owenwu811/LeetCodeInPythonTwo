#2899
#easy

#Given an integer array nums where nums[i] is either a positive integer or -1. We need to find for each -1 the respective positive integer, which we call the last visited integer.

#To achieve this goal, let's define two empty arrays: seen and ans.

#Start iterating from the beginning of the array nums.

#If a positive integer is encountered, prepend it to the front of seen.
#If -1 is encountered, let k be the number of consecutive -1s seen so far (including the current -1),
#If k is less than or equal to the length of seen, append the k-th element of seen to ans.
#If k is strictly greater than the length of seen, append -1 to ans.
#Return the array ans.

 

#Example 1:

#Input: nums = [1,2,-1,-1,-1]

#Output: [2,1,-1]

#my own solution using python3:

#follow the directions

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        negativeonec = 0
        seen = deque()
        res = []
        for n in nums:
           #print(n, seen)
            if n >= 0:
                negativeonec = 0
                seen.appendleft(n)
                continue
            elif n == -1:
                negativeonec += 1
                k = negativeonec
                print(seen, k, n)
                if k <= len(seen):
                    res.append(seen[k - 1])
                else:
                    res.append(-1)
                
        return res
