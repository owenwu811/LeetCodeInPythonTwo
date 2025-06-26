
#3595
#medium

#You are given an integer array nums. In this array:

#Exactly one element appears once.

#Exactly one element appears twice.

#All other elements appear exactly three times.

#Return an integer array of length 2, where the first element is the one that appears once, and the second is the one that appears twice.

#Your solution must run in O(n) time and O(1) space.



#my own solution using python3:

#create a frequency dictionary, and just follow the instructions

class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        print(c)
        for a, b in c.items():
            if b == 1:
                ans.insert(0, a)
            if b == 2:
                ans.insert(1, a)
        return ans
