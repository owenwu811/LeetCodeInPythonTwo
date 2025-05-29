#1387
#medium

#The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

#if x is even then x = x / 2
#if x is odd then x = 3 * x + 1
#For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

#Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

#Return the kth integer in the range [lo, hi] sorted by the power value.

#Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in a 32-bit signed integer.

 

#Example 1:

#Input: lo = 12, hi = 15, k = 2
#Output: 13
#Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)


#my own solution using python3:

#just brute force it

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        sl = SortedList()
        def f(num, cnt, orig):
            if num == 1:
                #print(orig, cnt)
                sl.add((cnt, orig))
                return cnt
            if num == 1:
                return cnt
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            f(num, cnt + 1, orig)

        for i in range(lo, hi + 1):
            num = i
            cnt = 0
            orig = i
            f(num, cnt, orig)
            #print(num, res)
        print(sl)
        return sl[k - 1][1]
