#970
#medium

#Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

#An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

#You may return the answer in any order. In your answer, each value should occur at most once.


#my own solution after using a trick from another solution:

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        if x == 1 and y == 1 and bound > x and bound > y:
            return [x + 1]
        upper = int(sqrt(bound))
        for i in range(1, upper):
            a, b = x, y
            curx, cury = 0, 0
            for i in range(curx, upper + 1):
                if a ** i > bound:
                    return list(res)
                if i > bound:
                    break
                for j in range(cury, upper + 1):
                    if j > bound:
                        break
                    ans = a ** i + b ** j
                    if ans > bound:
                        break
                    if ans not in res:
                        res.add(ans)
        if bound == x and bound != y:
            if x not in res:
                res.add(x)
        return list(res)
            
