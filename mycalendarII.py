
#731
#medium

#You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

#A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

#The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

#Implement the MyCalendarTwo class:
#
#MyCalendarTwo() Initializes the calendar object.
#boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

#Example 1:

#Input
#["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
#[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
#Output
#[null, true, true, true, false, true, true]

#correct python3 solution (could not solve):

class MyCalendarTwo:

    def __init__(self):
        self.d = defaultdict(int)
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.d[startTime] += 1
        self.d[endTime] -= 1
        cur = 0
        for a in sorted(self.d.keys()):
            cur += self.d[a]
            if cur >= 3:
                self.d[startTime] -= 1
                self.d[endTime] += 1
                return False
        return True
