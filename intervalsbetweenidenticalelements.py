#2121
#medium


#You are given a 0-indexed array of n integers arr.

#The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.

#Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].

#Note: |x| is the absolute value of x.

 

#Example 1:

#Input: arr = [2,1,3,1,2,3,3]
#Output: [4,2,7,2,4,4,5]
#Explanation:
#- Index 0: Another 2 is found at index 4. |0 - 4| = 4
#- Index 1: Another 1 is found at index 3. |1 - 3| = 2
#- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
#- Index 3: Another 1 is found at index 1. |3 - 1| = 2
#- Index 4: Another 2 is found at index 0. |4 - 0| = 4
#- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
#- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
#Example 2:

#Input: arr = [10,5,10,10]
#Output: [5,0,3,4]
#Explanation:
#- Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
#- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
#- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
#- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4


#my own solution using python3:

#map values to indicies, and prefixsum each value's indicies, and then binary search to find absolute values

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        res = []
        d = defaultdict(list)
        for i, a in enumerate(arr):
            d[a].append(i)
        ps = dict()
        for k in d:
            ps[k] = list(itertools.accumulate(d[k]))
        print(ps)
        for i, a in enumerate(arr):
            now = 0
            l = bisect_left(d[a], i)
            r = bisect_right(d[a], i)
            pref = ps[a]
            if l > 0:
                low = pref[l - 1]
                high = i * l
                now += (high - low)


            if r < len(d[a]):
                low = i * (len(d[a]) - r)
                if r <= 0:
                    high = pref[-1]
                else:
                    high = pref[-1] - pref[r - 1]

                now += (high - low)
            res.append(now)
        return res
