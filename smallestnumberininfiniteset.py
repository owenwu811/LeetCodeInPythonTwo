
#2336
#medium

#You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

#Implement the SmallestInfiniteSet class:

#SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
#int popSmallest() Removes and returns the smallest integer contained in the infinite set.
#void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.


#my own solution using python3 on (3/8/25) - originally solved August 10, 2024, but didn't include the file:

class SmallestInfiniteSet:

    def __init__(self):
        self.s = SortedList()
        for i in range(1, 1001):
            self.s.add(i)

    def popSmallest(self) -> int:
        #print(self.s)
        if self.s:
            a = self.s[0]
            self.s.pop(0)
            return a

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.add(num)
