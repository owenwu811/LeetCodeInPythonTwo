
#1943
#medium

#There is a long and thin painting that can be represented by a number line. The painting was painted with multiple overlapping segments where each segment was painted with a unique color. You are given a 2D integer array segments, where segments[i] = [starti, endi, colori] represents the half-closed segment [starti, endi) with colori as the color.

#The colors in the overlapping segments of the painting were mixed when it was painted. When two or more colors mix, they form a new color that can be represented as a set of mixed colors.

#For example, if colors 2, 4, and 6 are mixed, then the resulting mixed color is {2,4,6}.
#For the sake of simplicity, you should only output the sum of the elements in the set rather than the full set.

#You want to describe the painting with the minimum number of non-overlapping half-closed segments of these mixed colors. These segments can be represented by the 2D array painting where painting[j] = [leftj, rightj, mixj] describes a half-closed segment [leftj, rightj) with the mixed color sum of mixj.

#For example, the painting created with segments = [[1,4,5],[1,7,7]] can be described by painting = [[1,4,12],[4,7,7]] because:
#[1,4) is colored {5,7} (with a sum of 12) from both the first and second segments.
#[4,7) is colored {7} from only the second segment.
#Return the 2D array painting describing the finished painting (excluding any parts that are not painted). You may return the segments in any order.

#A half-closed segment [a, b) is the section of the number line between points a and b including point a and not including point b.

#Input: segments = [[1,4,5],[4,7,7],[1,7,9]]
#Output: [[1,4,14],[4,7,16]]

#my own solution using python3:

#use line sweep algo and try to follow the picture exactly

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        sl = set()
        ms, me = float('inf'), float('-inf')
        for s in segments:
            start, end, val = s[0], s[1], s[2]
            sl.add(start)
            sl.add(end)
            d[start] += val
            if start <= ms:
                ms = start
            d[end] -= val
            if end >= me:
                me = end
        sl = sorted(list(sl))
        print(sl, "sl")
        a = list(range(0, me + 1))
        big = a[-1]
        p = [0] * len(a)
        for s in segments:
            start, end, val = s[0], s[1], s[2]
            if 0 <= start <= big:
                p[start] += val
            if 0 <= end <= big:
                p[end] -= val
        k = list(itertools.accumulate(p))
        ms = float('inf')
        me = float('-inf')
        res = []
        for i in range(1, len(sl)):
            start, end = sl[i - 1], sl[i]
            ms = min(ms, start)
            me = max(me, end)
            print(k[start: end], "now")
            now = sum(k[start: end]) // (end - start)
            if now > 0:
                cur = [start, end, now]
                print(cur)
                res.append(cur)
        return res
