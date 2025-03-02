#1109
#medium


#There are n flights that are labeled from 1 to n.

#You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

#Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

 

#Example 1:

#Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
#Output: [10,55,45,25,25]
#Explanation:
#Flight labels:        1   2   3   4   5
#Booking 1 reserved:  10  10
#Booking 2 reserved:      20  20
#Booking 3 reserved:      25  25  25  25
#Total seats:         10  55  45  25  25
#Hence, answer = [10,55,45,25,25]



#my own solution using python3:

#use line sweep algo to avoid having to loop through entire subarray to increment

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        p = [0] * n
        print(p)
        for b in bookings:
            start, end, amount = b[0] - 1, b[1] - 1, b[2]
            print(start, end, amount)
            p[start] += amount
            if end + 1 < len(p):
                p[end + 1] -= amount
            
        print(p)
        return list(itertools.accumulate(p))
