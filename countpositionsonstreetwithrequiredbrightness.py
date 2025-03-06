
#2237
#medium

#You are given an integer n. A perfectly straight street is represented by a number line ranging from 0 to n - 1. You are given a 2D integer array lights representing the street lamp(s) on the street. Each lights[i] = [positioni, rangei] indicates that there is a street lamp at position positioni that lights up the area from [max(0, positioni - rangei), min(n - 1, positioni + rangei)] (inclusive).

#The brightness of a position p is defined as the number of street lamps that light up the position p. You are given a 0-indexed integer array requirement of size n where requirement[i] is the minimum brightness of the ith position on the street.

#Return the number of positions i on the street between 0 and n - 1 that have a brightness of at least requirement[i].

#Input: n = 5, lights = [[0,1],[2,1],[3,2]], requirement = [0,2,1,4,1]
#Output: 4


#my own solution using python3:

#use line sweep algo and read question carefully

class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        #[position, range]
        d = defaultdict(int)
        sr = sorted(list(set(requirement)))
        myset = set()
        orig = [0] * n
        print(sr)
        for l in lights:
            val = l[1]
            left = max(0, l[0] - l[1])
            right = min(n - 1, l[0] + l[1])
            print(left, right)
            if left >= 0:
                orig[left] += 1
            if right + 1 < len(orig): 
                orig[right + 1] -= 1
        print(orig)
        a = list(itertools.accumulate(orig))
        print(a)
        res = 0
        for i, val in enumerate(a):
            if val >= requirement[i]:
                res += 1
        return res
