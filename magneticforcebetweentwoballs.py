#1552
#medium


#In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

#Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

#Given the integer array position and the integer m. Return the required force.


#my own solution using python3:

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 0, position[-1] - position[0]
        ans = 0
        def isgood(mid):
            cnt = 1
            left = position[0]
            for i in range(1, len(position)):
                if position[i] - left >= mid:
                    left = position[i]
                    cnt += 1
                    if cnt >= m:
                        return True

            return False

        while l <= r:
            mid = (l + r) // 2
            if isgood(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans
