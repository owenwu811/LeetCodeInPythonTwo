#1344
#medium

#Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

#Answers within 10-5 of the actual value will be accepted as correct.

#Input: hour = 12, minutes = 30
#Output: 165


#my own solution using python3:

#simulate the process knowing that a full circle is 360, and convert from hours to minutes and then fraction it by 360

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = hour % 12
        m = minutes % 60
        minuteangle = m / 60
        addition = ((1 / 12) * minuteangle)
        hourangle = (h / 12) + addition
        print(hourangle, minuteangle)
        first = hourangle * 360
        second = minuteangle * 360
        #print(first, second)
        diff = abs(second - first)
        print(diff, first, second, 360)
        return min(diff, abs(360 - diff))
