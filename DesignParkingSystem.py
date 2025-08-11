

#1603
#easy

#Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

#Implement the ParkingSystem class:

#ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
#bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

#my own solution using python3:

#be careful to just understand the requirements of going big to small instead of intuitive way

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cur = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        print(carType, self.cur)
        if carType == 1:
            if self.cur[0] > 0:
                self.cur[0] -= 1
                return True
            return False
        if carType == 2:
            if self.cur[1] > 0:
                self.cur[1] -= 1
                return True
            return False
        if carType == 3:
            if self.cur[2] > 0:
                self.cur[2] -= 1
                return True
            return False
 
