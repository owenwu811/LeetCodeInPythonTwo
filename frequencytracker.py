#2671

#medium

#Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

#Implement the FrequencyTracker class.

#FrequencyTracker(): Initializes the FrequencyTracker object with an empty array initially.
#void add(int number): Adds number to the data structure.
#void deleteOne(int number): Deletes one occurrence of number from the data structure. The data structure may not contain number, and in this case nothing is deleted.
#bool hasFrequency(int frequency): Returns true if there is a number in the data structure that occurs frequency number of times, otherwise, it returns false.


#my own solution that got TLE 1115/1118:

class FrequencyTracker:

    def __init__(self):
        self.d = defaultdict(int)

    def add(self, number: int) -> None:
        self.d[number] += 1

        

    def deleteOne(self, number: int) -> None:
        if number in self.d:
            self.d[number] -= 1
            if self.d[number] == 0:
                del self.d[number]
        

    def hasFrequency(self, frequency: int) -> bool:
        #myset = set(self.d.values())
        #self.s = {value: key for key, value in self.d.items()}
        cur = SortedList(self.d.values())
        l, r = 0, len(cur) - 1
        while l <= r:
            mid = (l + r) // 2
            if cur[mid] == frequency:
                return True
            elif cur[mid] > frequency:
                r = mid - 1
            else:
                l = mid + 1
        return False
        #return frequency in self.d.values()
        



#correct python3 solution:

class FrequencyTracker:

    def __init__(self):
        self.numbers = Counter()  # Number -> frequency
        self.freqs = defaultdict(set)  # Freq -> numbers with this frequency.
        

    def add(self, number: int) -> None:
        freq = self.numbers[number]  # 0 if not in there.
        self.freqs[freq].discard(number)  # Remove from old freq. In case it was 0 and didn't exist, use discard.

        # Update frequency to new value.
        self.freqs[freq + 1].add(number)
        self.numbers[number] += 1

    def deleteOne(self, number: int) -> None:
        if self.numbers[number] > 0:  # Cannot go below 0.
            self.freqs[self.numbers[number]].remove(number)  # Remove frequency first. Important.
            self.numbers[number] -= 1
            self.freqs[self.numbers[number]].add(number)  # Add back. In case it was 0 already, this will works.

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freqs[frequency]) > 0
        #return bool(len(self.freqs[frequency]))



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
