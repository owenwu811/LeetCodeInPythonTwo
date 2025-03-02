
#1094
#medium

#There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

#You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

#Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

#Example 1:

#Input: trips = [[2,1,5],[3,3,7]], capacity = 4
#Output: false


#my own solution using python3:

#use difference array technique minus one for end because the drop off point is inclusive 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        smallest = float('inf')
        largest = float('-inf')
        for t in trips:
            smallest = min(smallest, t[1])
            largest = max(largest, t[2])
        print(smallest, largest)
        dist = largest - smallest + 1
        a = [0] * dist
        for t in trips:
            start, end = t[1], t[2]
            if start >= 0 and start < len(a):
                a[start] += t[0]
            if end < len(a):
                a[end] -= t[0]
        print(a)
        h = list(itertools.accumulate(a))
        print(h)
        return max(h) <= capacity
