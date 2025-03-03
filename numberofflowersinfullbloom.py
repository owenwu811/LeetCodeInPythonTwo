
#2251
#hard

#You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

#Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.


#correct python3 solution (could not solve):

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = SortedList()
        ends = SortedList()
        for f in flowers:
            starts.add(f[0])
            ends.add(f[1])
        res = []
        for p in people:
            l = bisect_right(starts, p)
            r = bisect_left(ends, p)
            print(l, r)
            res.append(l - r)
        return res
