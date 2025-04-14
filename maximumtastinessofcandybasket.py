#2517
#medium


#You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

#The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

#Return the maximum tastiness of a candy basket.

 

#Example 1:

#Input: price = [13,5,1,8,21,2], k = 3
#Output: 8
#Explanation: Choose the candies with the prices [13,5,21].
#The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
#It can be proven that 8 is the maximum tastiness that can be achieved.



#correct python3 solution (could not solve):

class Solution:
    def maximumTastiness(self, p: List[int], k: int) -> int:
        p.sort()
        l, r = 0, p[-1] - p[0]
        def isgood(mid):
            cnt = 1
            left = p[0]
            for i in range(1, len(p)):
                if p[i] - left >= mid:
                    left = p[i]
                    cnt += 1
                    if cnt >= k:
                        return True
            return False

        res = 0
        while l <= r:
            mid = (l + r) // 2
            if isgood(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res
