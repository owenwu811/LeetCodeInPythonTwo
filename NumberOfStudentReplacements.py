

#3616
#medium

#You are given an integer array ranks where ranks[i] represents the rank of the ith student arriving in order. A lower number indicates a better rank.

#Initially, the first student is selected by default.

#A replacement occurs when a student with a strictly better rank arrives and replaces the current selection.

#Return the total number of replacements made.

#my own solution using python3:

#just loop through from 2nd to end, and count the number of ones smaller than the smallest one seen

class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        cur = ranks[0]
        ans = 0
        for a in ranks[1:]:
            if a < cur:
                cur = a
                ans += 1
        return ans
