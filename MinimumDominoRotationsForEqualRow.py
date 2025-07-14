#1007
#medium

#In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

#We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

#Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

#If it cannot be done, return -1.

#my own solution using python3:

#look at which one is less expensive to get

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t = Counter(tops)
        b = Counter(bottoms)
        tv = max(t.values())
        bv = max(b.values())
        ta = []
        for a, bb in t.items():
            if bb == tv:
                ta.append(a)
        ba = []
        for a, bbb in b.items():
            if bbb == bv:
                ba.append(a)
        bigger = max(tv, bv)
        ans = 0
        if bigger == tv and bigger != bv:
            for i in range(len(tops)):
                if tops[i] != ta[0]:
                    if bottoms[i] == ta[0]:
                        tops[i], bottoms[i] = bottoms[i], tops[i]
                        ans += 1
            if len(set(tops)) == 1:
                return ans
            else:
                return -1
        elif bigger == bv and bigger != tv:
            for i in range(len(bottoms)):
                if bottoms[i] != ba[0]:
                    if tops[i] == ba[0]:
                        bottoms[i], tops[i] = tops[i], bottoms[i]
                        ans += 1
            if len(set(bottoms)) == 1:
                return ans
            else:
                return -1
        else:
            print(ta, ba)
            if len(ta) > len(ba):
                for i in range(len(bottoms)):
                    if bottoms[i] != ba[0]:
                        if tops[i] == ba[0]:
                            bottoms[i], tops[i] = tops[i], bottoms[i]
                            ans += 1
                if len(set(bottoms)) == 1:
                    return ans
                else:
                    return -1
            else:
                for i in range(len(tops)):
                    if tops[i] != ta[0]:
                        if bottoms[i] == ta[0]:
                            tops[i], bottoms[i] = bottoms[i], tops[i]
                            ans += 1
                if len(set(tops)) == 1:
                    return ans
                else:
                    return -1
            





