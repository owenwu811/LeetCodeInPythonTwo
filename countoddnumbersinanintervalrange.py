
#1523
#easy

#Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

#Example 1:

#Input: low = 3, high = 7
#Output: 3
#Explanation: The odd numbers between 3 and 7 are [3,5,7].
#Example 2:

#Input: low = 8, high = 10
#Output: 1
#Explanation: The odd numbers between 8 and 10 are [9].


#my own solution using python3:

#simulate each condition instead of doing a loop to avoid TLE

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if high > 0 and low == 0:
            if high % 2 != 0:
                return high // 2 + 1
            else:
                return high // 2
        if high == low and low % 2 != 0 and high % 2 != 0:
            return 1
        if high % 2 != 0 and low % 2 != 0:
            diff = high - low
            return diff // 2 + 1
        if low % 2 != 0 and high % 2 == 0:
            return diff // 2 + 1
        if low % 2 == 0 and high % 2 != 0:
            return diff // 2 + 1
        if high % 2 == 0 and low % 2 == 0:
            return diff // 2
 
        else:
            return high - low
