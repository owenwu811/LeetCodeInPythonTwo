
#2349
#medium

#Design a number container system that can do the following:

#Insert or Replace a number at the given index in the system.
#Return the smallest index for the given number in the system.
#Implement the NumberContainers class:

#NumberContainers() Initializes the number container system.
#void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
#int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.


#my own solution using python3:

#use a sorted list to avoid tle

class NumberContainers:

    def __init__(self):
        self.d = SortedDict()
        self.sd = defaultdict(SortedList)
        self.seen = set()

    def change(self, index: int, number: int) -> None:
        if index in self.seen:
            val = self.d[index]
            self.sd[val].discard(index)
        self.d[index] = number
        self.sd[number].add(index)
        self.seen.add(index)
        
    def find(self, number: int) -> int:
        if number in self.sd:
            if self.sd[number]:
            #if len(self.sd[number]) >= 1:
                return self.sd[number][0]
                #return min(self.sd[number])
        return -1
        #SortedDict({}) 10
        #SortedDict({1: 10, 2: 10, 3: 10, 5: 10}) 10
        #SortedDict({1: 20, 2: 10, 3: 10, 5: 10}) 10
