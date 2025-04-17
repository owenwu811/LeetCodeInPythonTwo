#849
#medium

#You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

#There is at least one empty seat, and at least one person sitting.

#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

#Return that maximum distance to the closest person.

#Input: seats = [1,0,0,0,1,0,1]
#Output: 2

#my own solution using python3:

#greedily find the closest person using binary search without violating prior conditions

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ones = []
        zeros = []
        for i, s in enumerate(seats):
            if s == 1:
                ones.append(i)
            else:
                zeros.append(i)
        #print(ones)
        ans = 0
        for z in zeros:
           # print(z, ones)
            #bl = bisect_left(ones, z)
            br = bisect_left(ones, z)
            bl = br - 1
            flag = True
            if br < len(ones) and bl < len(ones):
                ll = ones[bl]
                mid = z
                rr = ones[br]
                if abs(mid - ll) < abs(mid - rr):
                    #print(abs(mid - ll), "here")
                    ans = max(ans, abs(mid - ll))
                    flag = False
                if abs(mid - ll) > abs(mid - rr):
                    #print(abs(mid - rr), "here")
                    ans = max(ans, abs(mid - rr))
                    flag = False
                if flag:
                    print(ll, mid, rr)
                    ans = max(ans, abs(ll - mid), abs(rr - mid))
            elif br < len(ones):
                rr = ones[br]
                ans = max(ans, abs(z - rr))
            else:
                ll = ones[bl]
                ans = max(ans, abs(z - ll))

        return ans
            
            #print(bl, br)
