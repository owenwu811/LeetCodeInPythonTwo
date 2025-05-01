
#732
#hard

#A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

#You are given some events [startTime, endTime), after each given event, return an integer k representing the maximum k-booking between all the previous events.

#Implement the MyCalendarThree class:

#MyCalendarThree() Initializes the object.
#int book(int startTime, int endTime) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
 

#Example 1:

#Input
#["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
#[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
#Output
#[null, 1, 1, 2, 3, 3, 3]


#my own solution using python3:

class MyCalendarThree:

    def __init__(self):
        self.d = defaultdict(int)
        #self.start = 1

    def book(self, startTime: int, endTime: int) -> int:
        self.d[startTime] += 1
        self.d[endTime] -= 1
        #print(self.d.values())
        cur = 0
        biggest = 0
        for a in sorted(self.d.keys()):
            cur += self.d[a]
            biggest = max(biggest, cur)
        return biggest
                
