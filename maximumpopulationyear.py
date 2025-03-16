
#1854
#easy

#You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

#The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

#Return the earliest year with the maximum population.

 

#Example 1:

#Input: logs = [[1993,1999],[2000,2010]]
#Output: 1993
#Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
#Example 2:

#Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
#Output: 1960
#Explanation: 
#The maximum population is 2, and it had happened in years 1960 and 1970.
#The earlier year between them is 1960.

#my own solution using python3:

#use line sweep

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        minstart = float('inf')
        maxend = float('-inf')
        for l in logs:
            minstart = min(minstart, l[0])
            maxend = max(maxend, l[1])
        a = list(range(minstart, maxend + 1))
        print(a)
        j = [0] * len(a)
        for l in logs:
            if l[0] in a:
                h = a.index(l[0])
                j[h] += 1
            if l[1] in a:
                h = a.index(l[1])
                j[h] -= 1
        k = list(itertools.accumulate(j))
        #print(k)
        biggest = max(k)
        print(k, biggest)
        for i in range(len(a)):
            if k[i] == biggest:
                return a[i]

