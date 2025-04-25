#475
#medium

#Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

#Every house can be warmed, as long as the house is within the heater's warm radius range. 

#Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

#Notice that all the heaters follow your radius standard, and the warm radius will the same.

 

#Example 1:

#Input: houses = [1,2,3], heaters = [2]
#Output: 1
#Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.


#my own solution using python3:

#use binary search and prefix sums

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = float('inf')
        if Counter(houses) <= Counter(heaters):
            return 0
        houses.sort()
        heaters.sort()
        upper = max(houses[-1], heaters[-1])
        orig = SortedSet(houses)
        l, r = 1, upper + 1

        while l <= r:
            radius = (l + r) // 2
            ll = float('inf')
            hh = float('-inf')
            a = [0] * len(houses)
            for heater in heaters:
                low = heater - radius
                high = heater + radius
                #print(low, high)
                lll = bisect_left(houses, low)
                rrr = bisect_right(houses, high) - 1

                #print(lll, rrr, "lll, rrr", houses)
                if lll >= 0 and lll < len(a):
                    a[lll] += 1
                if rrr + 1 < len(a):
                    a[rrr + 1] -= 1
                if lll <= rrr:
                    ll = min(ll, lll)
                    hh = max(hh, rrr)
            #print(a)
            b = list(itertools.accumulate(a))
            #print(b)
            #print("done", radius)
            #print(ll, hh)
            if min(b) > 0:
                ans = min(ans, radius)
                r = radius - 1
            else:
                l = radius + 1
        return ans
