#1090
#medium


#You are given n item's value and label as two integer arrays values and labels. You are also given two integers numWanted and useLimit.

#Your task is to find a subset of items with the maximum sum of their values such that:

#The number of items is at most numWanted.
#The number of items with the same label is at most useLimit.
#Return the maximum sum.

 

#Example 1:

#Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1

#Output: 9

#Explanation:

#The subset chosen is the first, third, and fifth items with the sum of values 5 + 3 + 1.



#my own solution using python3:

#simulate the process and sort it

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        d = defaultdict(list)
        cur = []
        for i in range(len(values)):
            heapq.heappush(d[labels[i]], -values[i])
            d[labels[i]].sort()
        for k in d:
            cur.append(d[k])
            #if d[labels[i]] not in cur:
            #    cur.append(d[labels[i]])
        print(d)
        cur.sort()
        print(cur, "cur")
        res = []
        orig = useLimit
        for c in cur:
            now = 0
            allowance = orig
            while allowance > 0:
                if c:
                    #if -1 * c[0] not in res:
                    res.append(-1 * heapq.heappop(c))
                allowance -= 1
        res.sort(reverse=True)
        print(res)
        return sum(res[:numWanted])
