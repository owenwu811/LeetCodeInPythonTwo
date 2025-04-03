
#1870
#medium

#You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

#Each train can only depart at an integer hour, so you may need to wait in between each train ride.

#For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
#Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

#Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.


#correct python3 solution (could not solve):

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        res = float('inf')
        l, r = 1, 10 ** 7
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for d in dist[:-1]:
                cur += int(ceil(d / mid))
            cur += (dist[-1] / mid)
            if cur <= hour:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        if res == float('inf'):
            return -1
        if int(res) > 10 ** 7: return -1
        return int(res) 
