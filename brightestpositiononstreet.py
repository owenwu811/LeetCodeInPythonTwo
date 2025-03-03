


#2021
#medium

#A perfectly straight street is represented by a number line. The street has street lamp(s) on it and is represented by a 2D integer array lights. Each lights[i] = [positioni, rangei] indicates that there is a street lamp at position positioni that lights up the area from [positioni - rangei, positioni + rangei] (inclusive).

#The brightness of a position p is defined as the number of street lamp that light up the position p.

#Given lights, return the brightest position on the street. If there are multiple brightest positions, return the smallest one.



#my own solution using python3:

#use a dictionary to map do the difference array technique, and then accumulate the dictionary values and take the max of dictionary values to find the anwser

class Solution:
    def brightestPosition(self, lights):
        d = defaultdict(int)
        smallest = float('inf')
        largest = float('-inf')
        biggestval = float('-inf')
        for l in lights:
            start = l[0] - l[1]
            end = l[0] + l[1]
            d[start] += 1
            biggestval = max(biggestval, d[start])
            smallest = min(smallest, start)
            d[end + 1] -= 1
            #print(d)
            biggestval = max(biggestval, d[end + 1])
            largest = max(largest, end)
            
        d = dict(sorted(d.items(), key=lambda x: (x[0], -x[1])))
        #a = list(range(smallest, largest + 1))
        h = list(itertools.accumulate(d.values()))
        j = list(d.keys())
        #print(a)
        biggest = max(h)
        print(h)
        print(j)
        for i, c in enumerate(h):
            if c == biggest:
                return j[i]
