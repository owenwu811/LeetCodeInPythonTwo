#2580
#medium


#You are given a 2D integer array ranges where ranges[i] = [starti, endi] denotes that all integers between starti and endi (both inclusive) are contained in the ith range.

#You are to split ranges into two (possibly empty) groups such that:

#Each range belongs to exactly one group.
#Any two overlapping ranges must belong to the same group.
#Two ranges are said to be overlapping if there exists at least one integer that is present in both ranges.

#For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.
#Return the total number of ways to split ranges into two groups. Since the answer may be very large, return it modulo 109 + 7.


#my own solution after reading hints in python3:

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        mod = ((10 ** 9) + 7)
        print(ranges)
        ans = [ranges[0]]
        for i in range(1, len(ranges)):
            if ranges[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], ranges[i][1])
            else:
                ans.append(ranges[i])
        return (2 ** len(ans)) % mod
