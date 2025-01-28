#3369
#hard

#Design a data structure that keeps track of the values in it and answers some queries regarding their mean, median, and mode.

#Implement the StatisticsTracker class.

#StatisticsTracker(): Initialize the StatisticsTracker object with an empty array.
#void addNumber(int number): Add number to the data structure.
#void removeFirstAddedNumber(): Remove the earliest added number from the data structure.
#int getMean(): Return the floored mean of the numbers in the data structure.
#int getMedian(): Return the median of the numbers in the data structure.
#int getMode(): Return the mode of the numbers in the data structure. If there are multiple modes, return the smallest one.
#Note:

#The mean of an array is the sum of all the values divided by the number of values in the array.
#The median of an array is the middle element of the array when it is sorted in non-decreasing order. If there are two choices for a median, the larger of the two values is taken.
#The mode of an array is the element that appears most often in the array.


#my own solution using python3:

class StatisticsTracker:

    def __init__(self):
        self.d = deque()
        self.s = SortedList()
        self.freq = defaultdict(int)
        self.biggestf = 0
        
    def addNumber(self, number: int) -> None:
        self.d.append(number)
        self.freq[number] += 1
        self.s.add(number)

    def removeFirstAddedNumber(self) -> None:
        if self.d:
            a = self.d.popleft()
            self.freq[a] -= 1
            if self.freq[a] == 0:
                del self.freq[a]

            if a in self.s:
                self.s.remove(a)
      
    def getMean(self) -> int:
        ans = floor(sum(self.d) // len(self.d))
        
        return ans
        
    def getMedian(self) -> int:
        if len(self.s) % 2 == 0:
            mid = len(self.s) // 2
            return self.s[mid]
        else:
            mid = len(self.s) // 2 
            if mid >= 0 and mid < len(self.s):
                return self.s[mid]
            else:
                return self.s[0]
        
    def getMode(self) -> int:
        biggest = max(self.freq.values())
        ans = float('inf')
        for a, b in self.freq.items():
            if b == biggest:
                ans = min(ans, a)
        return ans
        


# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()
